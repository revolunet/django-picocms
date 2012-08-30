from django.contrib import admin
from django.forms.models import ModelMultipleChoiceField
from mptt.admin import MPTTModelAdmin
from mptt.forms import TreeNodeChoiceField
from django.contrib.admin import SimpleListFilter, DateFieldListFilter
from django.forms.widgets import SelectMultiple
import models

#
# Custom CMS admin
#


class AdminCategoryFilter(SimpleListFilter):
    """ Filter models by category
        Only show categories with active models
    """
    title = 'CMS Category'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        res = model_admin.queryset(request).values_list('category__pk', 'category__title').order_by('category').distinct().order_by()
        return res

    def queryset(self, request, queryset):
        if request.GET.get('category'):
            return queryset.filter(category__pk=request.GET.get('category'))
        return queryset


class CMSModelAdmin(admin.ModelAdmin):
    """ This ModelAdmin adds tinyMce for HTMLField and HTMLBigField.
        We also remove any reference to self in the many to many fields.
        I don't ever want to link to myself, do i ?
        We also add some CMS related filters and search fields
    """
    list_display = ['__unicode__', 'category', 'position', 'active', 'anonymous_access']
    list_filter = (AdminCategoryFilter, 'active', 'anonymous_access', ('modified', DateFieldListFilter))
    search_fields = ['category__title', 'title']
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = ('/static/tiny_mce/tiny_mce.js',
                '/static/chosen/js/chosen.jquery.min.js',
                '/static/js/admin.js',
              )
        css = {
            'all': ('/static/chosen/css/chosen.css', '/static/css/admin.css')
        }

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        """ removes self entries in related M2M fields """
        form = super(CMSModelAdmin, self).get_form(request, obj, **kwargs)
        if obj and obj.pk:
            for field, field_def in form.base_fields.items():
                if isinstance(field_def, ModelMultipleChoiceField):
                    if getattr(obj, field).model == self.model:
                        form.base_fields[field].queryset = form.base_fields[field].queryset.exclude(pk=obj.pk).order_by('title', '-pk')
                    elif issubclass(getattr(obj, field).model, models.CMSModel):
                        form.base_fields[field].queryset = form.base_fields[field].queryset.order_by('title', '-pk')
        return form

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        kwargs['widget'] = SelectMultiple(attrs={'class': 'chosen-multiple', 'style': 'width:300px'})
        kwargs['help_text'] = ''
        return super(CMSModelAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """ replaces any MPTTModel FK with a special combo """
        from mptt.models import MPTTModel, TreeForeignKey

        if issubclass(db_field.rel.to, MPTTModel) \
                and not isinstance(db_field, TreeForeignKey) \
                and not db_field.name in self.raw_id_fields:
            queryset = db_field.rel.to.objects.all()
            defaults = dict(form_class=TreeNodeChoiceField, queryset=queryset)
            defaults.update(kwargs)
            kwargs = defaults
        return super(CMSModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class CategoryAdmin(MPTTModelAdmin):
    """ MPTT based Admin class to display and manage CMS categories """
    list_display = ['title', 'position']

    def get_form(self, request, obj=None, **kwargs):
        form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
        if obj and obj.pk:
            form.base_fields['parent'].queryset = form.base_fields['parent'].queryset.exclude(pk=obj.pk)
        return form


admin.site.register(models.CMSCategory, CategoryAdmin)
