var myDashboard = new Dashboard();
myDashboard.addWidget('thrukwidget1', 'Servicegroup', {
    getData: function () {
        var self = this;
        Dashing.utils.get('servicegroup_widget', function(data) {
            $.extend(self.scope, data);
            self.getWidget().css("backgroundColor", data.color);
        });
    },
    interval: 3000
});
myDashboard.addWidget('thrukwidget2', 'Servicegroup', {
   getData: function () {
        var self = this;
        Dashing.utils.get('sg_asdf', function(data) {
            $.extend(self.scope, data);
            self.getWidget().css("backgroundColor", data.color);
        });
   },
   interval: 3000
});
myDashboard.addWidget('sg_fdsa', 'Servicegroup', {
   getData: function () {
        var self = this;
        Dashing.utils.get('sg_fdsa', function(data) {
            $.extend(self.scope, data);
            self.getWidget().css("backgroundColor", data.color);
        });
   },
   interval: 3000
});
