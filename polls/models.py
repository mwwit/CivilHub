from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from locations.models import Location
from taggit.managers import TaggableManager
# Generic bookmarks
from bookmarks.handlers import library


class Poll(models.Model):
    """
    Base poll class - means entire poll.
    """
    title = models.CharField(max_length=128, unique=True)
    slug  = models.SlugField(max_length=128, unique=True)
    tags  = TaggableManager()
    question = models.TextField()
    creator  = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    multiple = models.BooleanField(default=False)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Poll, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('locations:poll',
            kwargs={
                'place_slug':self.location.slug,
                'slug': self.slug
            }
        )

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    """
    Single answer model.
    """
    answer = models.CharField(max_length=256)
    poll   = models.ForeignKey(Poll)

    def __unicode__(self):
        return self.answer


class AnswerSet(models.Model):
    """
    Remember user answers to generate some statistics.
    """
    poll = models.ForeignKey(Poll)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    answers = models.ManyToManyField(Answer, related_name='answers', blank=True)


# Allow users to bookmark content
library.register(Poll)
