(function(define) {
    define(['backbone'], function(Backbone) {
        'use strict';

        return Backbone.Model.extend({
            defaults: {
                modes: [],
                course: '',
                enrollment_start: '',
                number: '',
                content: {
                    overview: '',
                    display_name: '',
                    number: '',
                    short_description: 'Not defined',
                },
                start: '',
                image_url: '',
                org: '',
                id: '',
                is_new: '',
                self_paced: false,
                enrollment_end: '',
                end: '',
                difficulty: 'Not defined',
                course_category: 'Not defined',
                certificate_available_date: '',
            }
        });
    });
}(define || RequireJS.define));
