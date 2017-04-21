from django.db import models
from locations.models import Venue


class Organization(models.Model):
    name = models.CharField(max_length=128)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['slug']

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()
    notes = models.CharField(blank=True, max_length=1024)
    organization = models.ForeignKey(Organization)
    venue = models.ForeignKey(Venue)
    attendance = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['slug']

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=64)
    notes = models.CharField(blank=True, max_length=512)
    event = models.ForeignKey(Event)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['slug']

    def save(self, *args, **kwargs):
        if not self.pk and not self.slug:
            self.slug = self.event.slug + '-' + slugify(self.name)
        super(Card, self).save(*args, **kwargs)

    def __str__(self):
        return self.name + ' ' + self.event.name
