from django.db import models
from django.template.defaultfilters import slugify


class Country(models.Model):
    name = models.CharField(max_length=32, unique=True)
    iso = models.SlugField(max_length=2, unique=True)
    nationality = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "countries"
        ordering = ['name']

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=64, unique=True)
    iso = models.SlugField(max_length=8, unique=True)
    country = models.ForeignKey(Country)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64, unique=True)
    region = models.ForeignKey(Region)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ['slug']

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=64, unique=True)
    city = models.ForeignKey(City)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Venue, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    city = models.ForeignKey(City)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
