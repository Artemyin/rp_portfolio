from django.db import models


class Project(models.Model):
    """ORM model for Project"""
    title = models.CharField(max_length=180)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
