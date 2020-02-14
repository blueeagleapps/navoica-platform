(function(define) {
    'use strict';
    define('navoica-theme/js/discussions_management/views/discussions_dashboard_factory',
        ['jquery', 'navoica-theme/js/discussions_management/views/discussions',
            'navoica-theme/js/discussions_management/models/course_discussions_detail',
            'navoica-theme/js/discussions_management/models/course_discussions_settings'],
        function($, DiscussionsView, CourseDiscussionTopicDetailsModel, CourseDiscussionsSettingsModel) {
            return function() {
                var courseDiscussionSettings = new CourseDiscussionsSettingsModel(),
                    discussionTopicsSettings = new CourseDiscussionTopicDetailsModel(),
                    $discussionsManagementElement = $('.discussions-management'),
                    discussionsView;

                courseDiscussionSettings.url = $discussionsManagementElement.data('course-discussion-settings-url');
                discussionTopicsSettings.url = $discussionsManagementElement.data('discussion-topics-url');

                discussionsView = new DiscussionsView({
                    el: $discussionsManagementElement,
                    discussionSettings: courseDiscussionSettings,
                    context: {
                        courseDiscussionTopicDetailsModel: discussionTopicsSettings
                    }
                });

                courseDiscussionSettings.fetch().done(function() {
                    discussionTopicsSettings.fetch().done(function() {
                        discussionsView.render();
                    });
                });
            };
        });
}).call(this, define || RequireJS.define);

