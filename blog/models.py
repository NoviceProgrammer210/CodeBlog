from django.db import models

# Create your models here.

class blog(models.Model):
    sno  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=30)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " by "+self.author