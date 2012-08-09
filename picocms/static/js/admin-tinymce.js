

django.jQuery(function() {
    function loadLongEditors() {
        // long editors
        tinyMceConfig.editor_selector = 'mceLongEditor';
        tinyMceConfig.height = 600;
        delete tinyMceConfig.oninit;
        if (django.jQuery('.' + tinyMceConfig.editor_selector).length > 0) {
            tinyMCE.init(tinyMceConfig);
        }
    }
    var tinyMceConfig = {
        theme : "advanced",
        mode : "specific_textareas",
        editor_selector : "mceEditor",
        width: 800,
        height:200,
        theme_advanced_buttons1 : "bold,italic,underline,separator,strikethrough,justifyleft,justifycenter,justifyright,justifyfull,bullist,numlist,undo,redo,link,unlink",
        theme_advanced_buttons2 : "",
        theme_advanced_buttons3 : "",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        theme_advanced_resizing : true,
        oninit : loadLongEditors
    };

    if (django.jQuery('.' + tinyMceConfig.editor_selector).length > 0) {
        // load standard editors
        tinyMCE.init(tinyMceConfig);
    }
    else {
        loadLongEditors();
    }
    

});