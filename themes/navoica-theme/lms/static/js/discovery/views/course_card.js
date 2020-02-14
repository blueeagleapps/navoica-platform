(function(define) {
    define([
        'jquery',
        'underscore',
        'backbone',
        'gettext',
        'edx-ui-toolkit/js/utils/date-utils'
    ], function($, _, Backbone, gettext, DateUtils) {
        'use strict';

        function formatDate(date, userLanguage, userTimezone) {
            var context;
            context = {
                datetime: date,
                language: userLanguage,
                timezone: userTimezone,
                format: DateUtils.dateFormatEnum.shortDate
            };
            return DateUtils.localize(context);
        }

        return Backbone.View.extend({

            tagName: 'div',
            templateId: '#course_card-tpl',
            className: 'col-lg-3 mb-4',

            initialize: function(options) {
                this.meanings = options.meanings || {};
                this.tpl = _.template($(this.templateId)
                    .html());
            },

            render: function() {
                var data = _.clone(this.model.attributes);
                data.meanings = this.meanings;
                data['org_text'] = data['org'];
                if (data['organizer'] !== undefined) {
                    data['org_text'] = organizer_list[+data['organizer']];
                }

                var userLanguage = 'pl',
                    userTimezone = 'Europe/Warsaw';
                if (data.advertised_start !== undefined) {
                    data.start = data.advertised_start;
                } else {
                    data.start = formatDate(
                        new Date(data.start),
                        userLanguage,
                        userTimezone
                    );
                }

                data.end = formatDate(
                    new Date(data.end),
                    userLanguage,
                    userTimezone
                );

                data.enrollment_start = formatDate(
                    new Date(data.enrollment_start),
                    userLanguage,
                    userTimezone
                );

                if (new Date(data.enrollment_end) > new Date(Date.now())){
                    data.enrollment_flag = true
                } else {
                    data.enrollment_flag = false
                }

                data.enrollment_end = formatDate(
                    new Date(data.enrollment_end),
                    userLanguage,
                    userTimezone
                );
                if (data.content.short_description !== undefined) {
                    let MaxSignsNumber = 150;
                    if (data.content.short_description.length > MaxSignsNumber) {
                        data.content.short_description = data.content.short_description.substring(0, MaxSignsNumber) + "...";
                    }
                } else {
                        data.content.short_description = 'Not defined'
                    }

                data.difficulty = this.meanings.difficulty.terms[data.difficulty];
                data.availability = this.meanings.availability.terms[data.availability];
                data.course_category = this.meanings.course_category.terms[data.course_category];

                this.$el.html(this.tpl(data));
                return this;
            }

        });
    });
}(define || RequireJS.define));

