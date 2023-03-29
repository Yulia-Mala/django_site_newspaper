from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.username


class Newspaper(models.Model):
    title = models.CharField(max_length=63, unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField()
    topic = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    class Meta:
        ordering = ["-publish_date"]

    def __str__(self):
        return f"{self.title} date: {self.publish_date}"
