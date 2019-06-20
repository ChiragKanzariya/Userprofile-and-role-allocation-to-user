from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify

from wagtail.admin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalManyToManyField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet


@register_snippet
class Choice(models.Model):

    choice = models.CharField(max_length=255)

    panels = [
        FieldPanel('choice')
    ]

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name_plural = 'Choices'


class ProfileModel(Page):
    ROLE_CHOICES = (
        ('A', 'Admin'),
        ('N', 'Normal')
    )

    image = models.FileField(upload_to='static/upload/', blank=True, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    designation = ParentalManyToManyField(Choice, blank=True)
    other = models.TextField(max_length=250)

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('name'),
        FieldPanel('role'),
        FieldPanel('designation', widget=forms.CheckboxSelectMultiple),
        FieldPanel('other')
    ]

    def __str__(self):
        return str(self.name)

    # def clean(self):
    #     """Override the values of title and slug before saving."""
    #     # super(MatchPage, self).clean() # Python 2.X syntax
    #     super().clean()
    #     new_title = 'Match %s' % self.name
    #     self.title = new_title
    #     self.slug = slugify(new_title)

    class Meta:
        verbose_name = 'Profile Page'
        verbose_name_plural = 'Profile Pages'


# ProfileModel._meta.get_field('slug').default = 'default-blank-slug'
