var myDashboard = new Dashboard({widgetMargins: [5, 5], widgetBaseDimensions: [360, 300]});
myDashboard.addWidget('asdf', 'Servicegroup', {
    getData: function () {
        var self = this;
        Dashing.utils.get('sg_app_asdf', function(data) {
            $.extend(self.scope, data);
            self.getWidget().css("backgroundColor", data.color);
        });
    },
//    interval: 10000
});
myDashboard.addWidget('sg_app_fdsa', 'Servicegroup', {
   getData: function () {
        var self = this;
        Dashing.utils.get('sg_app_fdsa', function(data) {
            $.extend(self.scope, data);
            self.getWidget().css("backgroundColor", data.color);
        });
   },
//   interval: 10000
});
myDashboard.addWidget('sg_app_zxcv', 'Servicegroup', {
   getData: function () {
        var self = this;
        Dashing.utils.get('sg_app_zxcv', function(data) {
            $.extend(self.scope, data);
            self.getWidget().css("backgroundColor", data.color);
        });
   },
   interval: 10000
});
