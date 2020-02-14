(function(define) {
    'use strict';

    define(['navoica-theme/js/api_admin/views/catalog_preview'], function(CatalogPreviewView) {
        return function(options) {
            var view = new CatalogPreviewView({
                el: '.catalog-body',
                previewUrl: options.previewUrl,
                catalogApiUrl: options.catalogApiUrl
            });
            return view.render();
        };
    });
}).call(this, define || RequireJS.define);
