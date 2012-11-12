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
 - `CMSModel` abstract fields : active, anonymous_access, created, modified... see below
 - Easy instance rendering. Juste define `modelName.html` template and your instance will use it to render itself with the permalink.
 - Basic `HTMLField` and `HTMLBigField` for your models with tinyMCE
 - `Chosen` advanced select field for CMSModel foreignkeys in the admin
 - Ability to insert files in HTMLFields based on custom CMS File Models (eg: images)
 - South support

## When you inherit from a CMSModel, you get :

 - `active` attribute (boolean)
 - `anonymous_access` attribute (boolean)
 - `created` date/time of creation
 - `modified` date/time of creation
 - `modified_by` user who created/edited the entry
 - `category` a MPTT category
 - `position` enable manual ordering
 - `slug` slug field for your urls
 - `title` a title field
 - `CMSMeta` options:
     - `root_category` : when editing this object in the admin, categories will be this category or its descendants. Specify a string like `news` or `news/frontpage`.
     - `image_model`: specify any model with a `file` attribute that will be used for the image picker in the admin.


## Todo :

 - move up/down entry in the TreeAdmin
 - better admin UI for categories/entries management
 - template tags for HTML fragment
 - move to CBV style (or not)


 [0]: https://github.com/django-mptt/django-mptt/
