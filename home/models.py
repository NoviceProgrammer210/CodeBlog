from django.db import models

# Create your models here.
# table for storing data from contact us Page

class Contact(models.Model):
    sno  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phno = models.CharField(max_length=15)
    content = models.TextField()
    email = models.EmailField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from '+self.name + " with email "+self.email
