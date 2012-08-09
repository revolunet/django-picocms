from django.forms import Textarea
from django.db import models


class HTMLField(models.TextField):
    field_class = 'mceEditor'

    def formfield(self, **kwargs):
        kwargs.update(
            {"widget": Textarea(attrs={'class': self.field_class})}
        )
        return super(HTMLField, self).formfield(**kwargs)


class HTMLBigField(HTMLField):
    field_class = 'mceLongEditor'


try:
    # in case south is installed
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^simplecms\.fields\.HTMLField"])
    add_introspection_rules([], ["^simplecms\.fields\.HTMLBigField"])
except:
    pass
