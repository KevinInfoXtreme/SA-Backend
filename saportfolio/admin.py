from django.contrib import admin
from .models import Project, ProjectImage,Disponibilite


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Disponibilite)