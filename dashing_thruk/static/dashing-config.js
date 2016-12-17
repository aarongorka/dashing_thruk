var myDashboard = new Dashboard();
myDashboard.addWidget('thrukwidget1', 'Servicegroup', {
    getData: function () {
        var self = this;
        Dashing.utils.get('servicegroup_widget', function(data) {
            $.extend(self.scope, data);
        });
        Dashing.utils.get('servicegroup_widget', function(color) {
            self.getWidget().css("backgroundColor", color.color);
        });
    },
    interval: 3000
});
