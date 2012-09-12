django-picocms
================

This simple CMS can manage any model and organise them in various categories.

## Typical usage :

You need to organise various models in several categories/sub categories via the django admin.

## Installation :

 - install with `pip install git+https://github.com/revolunet/django-picocms.git`
 - add `picocms` to your `INSTALLED_APPS`
 - include picocms urls to your `urls.py` if you want to publish your models

in urls.py :

    urlpatterns += patterns('',
        url(r'', include('picocms.urls'))
    )

 - create your models based on the `CMSModel` abstract class

 - register your models for the admin :

in admin.py :

    admin.site.register(MyModel, picocms.admin.CMSModelAdmin)

 - you'll need [django-mptt][0]


## What you'll get for free :

 - Unlimited categories to organise your models with a simple AdminTreeView for categories ([django-mptt][0] based and no d&d yet)
 - `CMSModel` abstract fields : active, anonymous_access, created, modified, modified_by, position, category, title and slug
 - Easy instance rendering. Juste define `modelName.html` template and your instance will use it to render itself with the permalink.
 - Basic `HTMLField` and `HTMLBigField` for your models with tinyMCE
 - `Chosen` advanced select field for CMSModel foreignkeys in the admin
 - Ability to insert files in HTMLFields based on custom CMS File Models (eg: images)
 - South support


## Todo :

 - move up/down entry in the TreeAdmin
 - better admin UI for categories/entries management
 - template tags for HTML fragment
 - move to CBV style (or not)


 [0]: https://github.com/django-mptt/django-mptt/