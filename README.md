
django-picocms
================

This simple CMS can manage any model and organise them in various categories.

## Typical usage :

You need to organise various models in several categories/sub categories via the django admin.

## Installation :

 - add `picocms` to your `INSTALLED_APPS`
 - include picocms urls to your `urls.py` if you want to publish your models


    urlpatterns += patterns('',
        url(r'', include('picocms.urls'))
    )


 - create your models based on the `CMSModel` abstract class

 - register your models for the admin :

    admin.site.register(MyModel, picocms.admin.CMSModelAdmin)

 - you'll need [django-mptt][0]


## What you get for free :

 - Unlimited categories to organise your models with a simple AdminTreeView for categories ([django-mptt][0] based and no d&d yet)
 - `CMSModel` abstract fields : active, anonymous_access, created, modified, modified_by, position, category, title and slug
 - Easy instance rendering. Juste define `modelName.html` template and your instance will use it to render itself with the permalink.
 - Basic `HTMLField` and `HTMLBigField` for your models with tinyMCE
 - South support


## Todo :

 - move to CBV style
 - better admin UI for categories/entries management
 - template tags for HTML fragment


 [0]: https://github.com/django-mptt/django-mptt/