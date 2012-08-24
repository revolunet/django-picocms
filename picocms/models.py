# -*- encoding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template.base import TemplateDoesNotExist

from mptt.models import MPTTModel, TreeForeignKey


class CMSCategory(MPTTModel):
    """ This class represent a category of data. You can organise and order categories
        in the django admin with the django-mptt tree admin tool.
        Any CMSModel based django model will have a parent category.

    """
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    position = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['position']

    class Meta:
        verbose_name_plural = 'categories'


class ActiveModelManager(models.Manager):
    def for_user(self, user):
        """ check if model is active and accessible """
        qs = super(ActiveModelManager, self).get_query_set().filter(active=True)
        if user.is_anonymous():
            qs = qs.filter(anonymous_access=True)
        return qs


class CMSModel(models.Model):
    """ Abstract model with generic fields to handle content management in categories.
        Any model inheriting from
    """
    active = models.BooleanField(default=True)
    anonymous_access = models.BooleanField(default=True, verbose_name=u'Allow anonymous access')
    created = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, null=True, editable=False, on_delete=models.SET_NULL)
    modified = models.DateTimeField(auto_now=True)
    position = models.IntegerField(default=0)
    category = models.ForeignKey(CMSCategory, null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(db_index=True, unique=True, verbose_name=u'Unique url code')
    title = models.CharField(max_length=100)

    objects = ActiveModelManager()

    class Meta:
        abstract = True
        ordering = ['category__tree_id', 'category__lft', 'position', '-id', 'title']

    @models.permalink
    def get_absolute_url(self):
        link = ('picocms-view-detail', [self._meta.app_label, self.__class__.__name__, self.slug])
        return link

    def render(self, request):
        """ render entry based on its template """
        tpl_name = '%s.html' % self.__class__.__name__.lower()
        try:
            result = render(request, tpl_name, dictionary={
                'instance': self
            })
        except TemplateDoesNotExist:
            result = 'object: %s : template %s not found' % (self.title, tpl_name)
        return result

    @classmethod
    def _get_instance(cls, request, slug):
        """ check if instance exists and is accessible and returns it """
        try:
            return cls.objects.for_user(request.user).get(slug=slug)
        except cls.DoesNotExist:
            raise Http404('No %s matches the given query.' % cls._meta.object_name)

    @classmethod
    def get_response(cls, request, slug):
        """ return entry associated response """
        instance = cls._get_instance(request, slug)
        return HttpResponse(instance.render(request))

    def __unicode__(self):
        return self.title
