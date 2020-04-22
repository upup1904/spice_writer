from django.db import models


class LinerNote(models.Model):
    title = models.CharField(max_length=100, unique=False, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)



class Line(models.Model):
    episode = models.IntegerField()
    line = models.IntegerField()
    slug = models.SlugField(max_length=100)
    text = models.TextField(max_length=300, blank=True, null=True)
    varies_from_gabler = models.BooleanField(null=True, blank=True)
    liner_notes = models.ManyToManyField(LinerNote)
 

    class Meta:
        unique_together = ('episode', 'line')
