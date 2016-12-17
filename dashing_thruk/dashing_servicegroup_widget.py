#!/usr/bin/env python
from dashing.widgets import ListWidget
from django.conf import settings

problems = 'CRITICAL'

class ServicegroupWidget(ListWidget):
    title = 'A Servicegroup'
    more_info = 'Servicegroup Description'

    def get_updated_at(self):
        return 'Last updated at: test'

    def get_data(self):
        if problems:
            return [{'label':settings.THRUK_URL, 'value':'testvalue'}]
        else:
            return

    def get_status(self):
        if problems:
            return problems
        else:
            return 'OK'

    def get_color(self):
        if problems:
            return "red"
        else:
            return "green"

    def get_context(self):
        return {
            'title': self.get_title(),
            'status': self.get_status(),
            'moreInfo': self.get_more_info(),
            'updatedAt': self.get_updated_at(),
            'data': self.get_data(),
            'color': self.get_color(),
        }

class sg_asdf(ServicegroupWidget):
    def get_color(self):
        return 'green'
    def get_title(self):
        return self.__class__.__name__ # call this separately and replace with proper name
