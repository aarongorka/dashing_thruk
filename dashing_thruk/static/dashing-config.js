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
myDashboard.addWidget('thrukwidget2', 'Servicegroup', {
   getData: function () {
        var self = this;
        Dashing.utils.get('sg_asdf', function(data) {
            $.extend(self.scope, data);
        });
        //$.extend(this.scope, {
        //    title: 'Buzzwords',
        //    more_info: '# of times said around the office',
        //    updated_at: 'Last updated at 18:58',
	//    color: 'blue',
        //    status: 'OK',
        //    data: [{label: 'Exit strategy', value: 24},
        //           {label: 'Web 2.0', value: 12},
        //           {label: 'Turn-key', value: 2},
        //           {label: 'Enterprise', value: 12},
        //           {label: 'Pivoting', value: 3},
        //           {label: 'Leverage', value: 10},
        //           {label: 'Streamlininess', value: 4},
        //           {label: 'Paradigm shift', value: 6},
        //           {label: 'Synergy', value: 7}]
	//});
        var self = this;
        Dashing.utils.get('sg_asdf', function(color) {
            self.getWidget().css("backgroundColor", color.color);
        });
   },
   interval: 3000
});
