from django.db import models

# Create your models here. (see: https://docs.djangoproject.com/en/4.0/ref/models/fields/)
# Note: changes here will show in admin portal!


class Project(models.Model):
    title = models.CharField(max_length=100)  # properties
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        # display titles in admin portal ( http://127.0.0.1:8000/admin/portfolio/project/ )
        return self.title
