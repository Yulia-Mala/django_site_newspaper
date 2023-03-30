from django.contrib.auth.models import AbstractUser
from django.db import models


from django_site_newspaper.settings import AUTH_USER_MODEL


class Topic(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username


class Newspaper(models.Model):
    title = models.CharField(max_length=63, unique=True)
    content = models.TextField()
    publish_date = models.DateField(null=True, blank=True)
    topic = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="newspapers"
    )

    class Meta:
        ordering = ["-publish_date"]

    def __str__(self):
        return f"{self.title} date: {self.publish_date}"
