from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    owner = models.ForeignKey(User, verbose_name="user", related_name="Post")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date',)
