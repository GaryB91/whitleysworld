from __future__ import unicode_literals

from django.db import models


class Story(models.Model):
    """ Story model """
    title = models.CharField(max_length=50)
    date_published = models.DateField(auto_now_add=True)
    slug = models.SlugField()


class Page(models.Model):
    """ Page model """
    story = models.ForeignKey(
        to='story.Story',
        related_name='pages'
    )
    number = models.PositiveIntegerField()
    content = models.TextField()

    class Meta:
        """ meta """
        unique_together = ('story', 'number')

