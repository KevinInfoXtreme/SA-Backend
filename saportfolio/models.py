from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()  # No upload_to needed

    def __str__(self):
        return self.title