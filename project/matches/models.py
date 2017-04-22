from django.db import models
from django.core.validators import MaxValueValidator
from events.models import Card, Title
from people.models import Fighter, Judge, Referee


class Match(models.Model):
    card = models.ForeignKey(Card)
    title = models.ForeignKey(Title, blank=True)
    weight_max = models.PositiveIntegerField(
        blank=True, validators = [MaxValueValidator(300)])
    round = models.PositiveIntegerField(
        blank=True, validators = [MaxValueValidator(10)])
    time_seconds = models.PositiveIntegerField(
        blank=True,
        validators = [MaxValueValidator(10)])
    draw = models.BooleanField(default=False)
    no_contest = models.BooleanField(default=False)
    METHODS = (
        (u'KO', u'Knockout'),
        (u'TKO', u'Technical Knockout'),
        (u'UD', u'Unanimous Decision'),
        (u'SD', u'Split Decision'),
        (u'MD', u'Majority Decision'),
        (u'ED', u'Extra Round Decision'),
        (u'UDr', u'Unanimous Draw'),
        (u'MDr', u'Majority Draw'),
        (u'NC', u'No Contest'),
        )
    method = models.CharField(max_length=3, choices=METHODS, blank=True)
    method_detail = models.CharField(max_length=64, blank=True)
    fighter1 = models.ForeignKey(Fighter, related_name='fighter1')
    fighter2 = models.ForeignKey(Fighter, related_name='fighter2')
    referee = models.ForeignKey(Referee, blank=True)
    video = models.URLField(blank=True)

    class Meta:
        ordering = ['-card__event__date']
        verbose_name_plural = "matches"

    def __str__(self):
        return '%s vs %s' % (self.fighter1.slug, self.fighter2.slug)


class ScoreCard(models.Model):
    winner_score = models.PositiveIntegerField(
        validators = [MaxValueValidator(200)])
    loser_score = models.PositiveIntegerField(
        validators = [MaxValueValidator(200)])
    match = models.ForeignKey(Match)
    judge = models.ForeignKey(Judge, blank=True)

    def __str__(self):
        return '%s-%s: %s vs %s' % (
            str(self.winner_score), str(self.loser_score),
            self.match.fighter1.slug, self.match.fighter1.slug)
