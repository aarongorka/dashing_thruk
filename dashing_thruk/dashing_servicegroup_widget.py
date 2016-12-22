#!/usr/bin/env python
from dashing.widgets import ListWidget
from django.conf import settings
import time
import urllib, json
import logging
import sys
import datetime

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

class ServicegroupWidget(ListWidget):
    servicegroup = ''
    title = ''
    more_info = ''
    start = ''
    finish = ''
    time_taken = ''
    last_updated = ''
    host_problems = []
    service_problems = []

    def __init__(self):
        self.servicegroup = self.__class__.__name__
        logging.debug('{}: Beginning __init__'.format(self.servicegroup))
        split_thruk_url = settings.THRUK_URL.split('//', 1)
        logging.info(split_thruk_url)
        priv_thruk_url = '{}//{}:{}@{}/cgi-bin/status.cgi?servicegroup={}&style=detail&view_mode=json'.format(split_thruk_url[0], settings.THRUK_USERNAME, settings.THRUK_PASSWORD, split_thruk_url[1], self.servicegroup)
        logging.debug('{}: Thruk URL: {}'.format(self.servicegroup, priv_thruk_url))
        start = time.time()
        logging.debug('{}: Beginning RESTful request at {}.'.format(self.servicegroup, start))
        try:
            result = urllib.urlopen(priv_thruk_url)
            r = json.load(result.fp)
            result.close()
        except:
            raise Exception('{}: Error accessing Thruk'.format(self.servicegroup))
        finish = time.time()
        logging.debug('{}: Finished RESTful request at {}.'.format(self.servicegroup, finish))

        if r:
            logging.info('{}: JSON data successfully retrieved'.format(self.servicegroup))
            self.last_updated = datetime.datetime.fromtimestamp(finish).strftime('%H:%M:%S')
            self.time_taken = finish - start
            logging.info('{}: Time taken: {}'.format(self.servicegroup, self.time_taken))
        else:
            raise Exception('{}: Error with JSON response'.format(self.servicegroup))

        self.host_problems = []
        self.service_problems = []

        self.service_problems = [ x for x in r if x['state'] != 0 ]
        self.host_problems = [ x for x in r if x['host_state'] != 0 and x['host_state'] != 1 ]
        logging.debug('{}: service_problems: {}'.format(self.servicegroup, self.service_problems))
        logging.debug('{}: host_problems: {}'.format(self.servicegroup, self.host_problems))

        self.down_unack = [ x for x in r if (x['host_state'] != 0 and x['host_state'] != 1 and x['host_acknowledged'] == 0 and x['host_scheduled_downtime_depth'] == 0) ]

        self.unknown_unack = [ x for x in r if (x['state'] == 3 and x['acknowledged'] == 0 and x['host_scheduled_downtime_depth'] == 0 and x['scheduled_downtime_depth'] == 0) ]
        self.critical_unack = [ x for x in r if (x['state'] == 2 and x['acknowledged'] == 0 and x['host_scheduled_downtime_depth'] == 0 and x['scheduled_downtime_depth'] == 0) ]
        self.warning_unack = [ x for x in r if (x['state'] == 1 and x['acknowledged'] == 0 and x['host_scheduled_downtime_depth'] == 0 and x['scheduled_downtime_depth'] == 0) ]

        self.down_ack = [ x for x in r if (x['host_state'] != 0 and x['host_state'] != 1 and (x['host_acknowledged'] != 0 or x['host_scheduled_downtime_depth'] != 0)) ]

        self.unknown_ack = [ x for x in r if (x['state'] == 3 and (x['acknowledged'] != 0 or x['host_scheduled_downtime_depth'] != 0 or x['scheduled_downtime_depth'] != 0)) ]
        self.critical_ack = [ x for x in r if (x['state'] == 2 and (x['acknowledged'] != 0 or x['host_scheduled_downtime_depth'] != 0 or x['scheduled_downtime_depth'] != 0)) ]
        self.warning_ack = [ x for x in r if (x['state'] == 1 and (x['acknowledged'] != 0 or x['host_scheduled_downtime_depth'] != 0 or x['scheduled_downtime_depth'] != 0)) ]
        
        self.more_info = self.servicegroup

    # Thruk does not expose information about servicegroups via its API, so
    def get_title(self):
        return self.title

    def get_more_info(self):
        return self.more_info

    def get_updated_at(self):
        return 'Last updated at: {} (took {:.1f}s)'.format(self.last_updated, round(self.time_taken, 2))

    def get_data(self):
        table = []
        for problem in self.host_problems:
#            table.append({'label':'{:.20}'.format(problem['host_display_name']), 'value':'DOWN'})
            table.append({'label':'{}'.format(problem['host_display_name']), 'value':'DOWN'})
        for problem in self.service_problems:
#            table.append({'label':'{:.20}'.format(problem['host_display_name']), 'value':'{:.20}s'.format(problem['description'])})
            table.append({'label':'{}'.format(problem['host_display_name']), 'value':'{}s'.format(problem['description'])})
        return table

    def get_status(self):
        if self.down_unack:
            return 'DOWN'
        elif self.unknown_unack:
            return 'UNKNOWN'
        elif self.critical_unack:
            return 'CRITICAL'
        elif self.warning_unack:
            return 'WARNING'
        elif self.down_ack:
            return 'DOWN (ACKNOWLEDGED)'
        elif self.unknown_ack:
            return 'UNKNOWN (ACKNOWLEDGED)'
        elif self.critical_ack:
            return 'CRITICAL (ACKNOWLEGED)'
        elif self.warning_ack:
            return 'WARNING (ACKNOWLEGED)'
        else:
            return 'OK'

    def get_color(self):
        if self.down_unack:
            return '#ff5b33' # red
        elif self.unknown_unack:
            return '#ff9e00' # orange
        elif self.critical_unack:
            return '#ff5b33' # red
        elif self.warning_unack:
            return '#ffde00' # yellow
        elif self.down_ack or self.unknown_ack or self.critical_ack or self.warning_ack:
            return 'pink'
        else:
            return '#0f3' # green

    def get_url(self):
        return '{}/cgi-bin/status.cgi?servicegroup={}&style=detail&sortoption=3&sorttype=2'.format(settings.THRUK_URL, self.servicegroup)

    def get_context(self):
        return {
            'title': self.get_title(),
            'status': self.get_status(),
            'moreInfo': self.get_more_info(),
            'updatedAt': self.get_updated_at(),
            'data': self.get_data(),
            'color': self.get_color(),
            'url': self.get_url(),
        }

class sg_app_asdf(ServicegroupWidget):
    title = 'Asdf Servicegroup'

class sg_app_fdsa(ServicegroupWidget):
    title = 'Fdsa Servicegroup'

class sg_app_zxcv(ServicegroupWidget):
    title = 'Zxcv Servicegroup'
