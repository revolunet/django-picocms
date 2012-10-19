
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
        theme_advanced_buttons1 : "bold,italic,underline,fontsizeselect,separator,justifyleft,justifycenter,justifyright,justifyfull,separatort,separator,imagecms,link,unlink,forecolor,backcolor",
        theme_advanced_buttons2 : "bullist,numlist,outdent,indent,sub,sup,charmap,hr,removeformat,separator,undo,redo,separator,code",
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

    django.jQuery('.chosen-multiple').chosen();
    django.jQuery('.chosen-multiple ~ a.add-another').hide();

});
