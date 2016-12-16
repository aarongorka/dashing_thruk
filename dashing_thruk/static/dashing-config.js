var myDashboard = new Dashboard();
myDashboard.addWidget('thrukwidget1', 'List', {
    getData: function () {
        var self = this;
        Dashing.utils.get('servicegroup_widget', function(data) {
            $.extend(self.scope, data);
        });
    	this.getWidget().css("backgroundColor", "red");
    },
    interval: 3000
});
