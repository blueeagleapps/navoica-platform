(function(define) {
    define([
        'jquery',
        'underscore',
        'backbone',
        'gettext',
        'navoica-theme/js/discovery/models/filter',
        'navoica-theme/js/discovery/views/filter_label'
    ], function($, _, Backbone, gettext, Filter, FilterLabel) {
        'use strict';

        return Backbone.View.extend({

            el: '#filter-bar',
            templateId: '#filter_bar-tpl',

            events: {
                'click #clear-all-filters': 'clearAll',
                'click li .discovery-button': 'clearFilter'
            },

            initialize: function() {
                this.tpl = _.template($(this.templateId).html());
                this.render();
                this.listenTo(this.collection, 'remove', this.hideIfEmpty);
                this.listenTo(this.collection, 'add', this.addFilter);
                this.listenTo(this.collection, 'reset', this.resetFilters);
            },

            render: function() {
                this.$el.html(this.tpl());
                this.$ul = this.$el.find('ul');
                this.$el.addClass('is-animated');
                return this;
            },

            addFilter: function(filter) {
                var label = new FilterLabel({model: filter});
                this.$ul.append(label.render().el);
                this.show();
		document.getElementById('clear-all-filters').style.display = 'block';
            },

            hideIfEmpty: function() {
                if (this.collection.isEmpty()) {
                    this.hide();
                }
            },

            resetFilters: function() {
                this.$ul.empty();
                this.hide();
		document.getElementById('clear-all-filters').style.display = 'none';
            },

            clearFilter: function(event) {
                var $target = $(event.currentTarget);
                var filter = this.collection.get($target.data('type'));
                this.trigger('clearFilter', filter.id);
		document.getElementById('clear-all-filters').style.display = 'none';
            },

            clearAll: function(event) {
                this.trigger('clearAll');
		document.getElementById('clear-all-filters').style.display = 'none';
            },

            show: function() {
                this.$el.removeClass('is-collapsed');
            },

            hide: function() {
                this.$ul.empty();
                this.$el.addClass('is-collapsed');
		document.getElementById('clear-all-filters').style.display = 'none';
            }

        });
    });
}(define || RequireJS.define));
