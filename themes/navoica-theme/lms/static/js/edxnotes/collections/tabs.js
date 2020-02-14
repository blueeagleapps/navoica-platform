(function(define, undefined) {
    'use strict';
    define([
        'backbone', 'navoica-theme/js/edxnotes/models/tab'
    ], function(Backbone, TabModel) {
        var TabsCollection = Backbone.Collection.extend({
            model: TabModel
        });

        return TabsCollection;
    });
}).call(this, define || RequireJS.define);
