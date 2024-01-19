from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class jobpost(models.Model):
   
    Titel = models. CharField(max_length=100)
    Description = models.CharField(max_length=400)
    company = models.CharField(max_length=100)
    postes_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    type = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    Roles = models.TextField(max_length=1000)

    def __str__(self):
        return self.Titel


    def get_absolute_url(self):
        return reverse ("detail",kwargs={'pk' : self.pk})
    
class apply(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    phone_no = models.BigIntegerField()