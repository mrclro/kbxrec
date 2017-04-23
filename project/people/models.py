from django.core.validators import MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify
from locations.models import City, Country, Team
from events.models import Title


class Alias(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "aliases"
        ordering = ['name']

    def __str__(self):
        return self.name


class Referee(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Judge(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Fighter(models.Model):
    SEXES = ((u'M', u'Male'), (u'F', u'Female'),)
    sex = models.CharField(max_length=2, choices=SEXES, default=SEXES[0][0])
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_name = models.CharField(blank=True, max_length=256)
    alias = models.ManyToManyField(Alias, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.ForeignKey(City, related_name='birth_place',
                                    blank=True, null=True)
    nationality = models.ManyToManyField(Country, blank=True)
    height = models.PositiveIntegerField(blank=True, null=True,
                                         validators = [MaxValueValidator(250)])
    reach = models.PositiveIntegerField(blank=True, null=True,
                                        validators = [MaxValueValidator(300)])
    team = models.ManyToManyField(Team, blank=True)
    trainer = models.ManyToManyField(Trainer, blank=True)
    residence = models.ForeignKey(City, related_name='residence',
                                  blank=True, null=True)
    STANCES = ((u'O', u'Orthodox'), (u'S', u'Southpaw'),)
    stance = models.CharField(max_length=2, blank=True, choices=STANCES)
    current_titles = models.ManyToManyField(Title, blank=True,
                                            related_name='current_titles')
    past_titles = models.ManyToManyField(Title, blank=True,
                                            related_name='past_titles')
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    website = models.URLField(blank=True)
    mma_record = models.URLField(blank=True)
    boxing_record = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.full_name
