from django.db import models

# Create your models here.
# Note: changes here will show in admin portal!


class Blog(models.Model):
    title = models.CharField(max_length=200)  # properties
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        # display titles in admin portal ( http://127.0.0.1:8000/admin/blog/blog/ )
        return self.title
