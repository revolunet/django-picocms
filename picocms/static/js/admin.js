
django.jQuery(function() {

    function getMceConfig(customConfig) {
        var tinyMceConfig = {
            theme : "advanced",
            mode : "specific_textareas",
            width: 800,
            height:200,
            plugins : "paste",
            paste_auto_cleanup_on_paste : true,
            paste_remove_spans: true,
            paste_remove_styles: true,
            paste_strip_class_attributes: true,
            theme_advanced_buttons1 : "bold,italic,underline,fontsizeselect,separator,justifyleft,justifycenter,justifyright,justifyfull,separatort,separator,imagecms,link,unlink,forecolor,backcolor",
            theme_advanced_buttons2 : "bullist,numlist,outdent,indent,sub,sup,charmap,hr,removeformat,separator,undo,redo,separator,code,separator,pastetext,pasteword,selectall",
            theme_advanced_buttons3 : "",
            theme_advanced_toolbar_location : "top",
            theme_advanced_toolbar_align : "left",
            theme_advanced_resizing : true
        };
        return django.jQuery.extend({}, tinyMceConfig, customConfig || {});

    }

    function mceInit(cls, mceParams) {
        mceParams = mceParams || {};
        if (django.jQuery('textarea.' + cls).length > 0) {
            mceParams.editor_selector = cls;
            tinyMCE.init(getMceConfig(mceParams));
        }
    }

    mceInit("mceEditor");
    mceInit("mceLongEditor", {height: 600});

    django.jQuery('.chosen-multiple').chosen();
    django.jQuery('.chosen-multiple ~ a.add-another').hide();

});
