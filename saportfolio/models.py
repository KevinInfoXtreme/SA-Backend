from django.db import models
from cloudinary.models import CloudinaryField  # optional, or use ImageField


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.project.title}"
    

class Disponibilite(models.Model):
    date = models.DateField(unique=True)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {'Disponible' if self.is_available else 'Indisponible'}"