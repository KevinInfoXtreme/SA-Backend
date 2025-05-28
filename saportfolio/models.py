from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='project_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title