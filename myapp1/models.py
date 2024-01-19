from django.db import models
from django.contrib.auth.models import User


class imgpro(models.Model):
    img = models.ImageField(upload_to='userimg/',blank=True)


class author(models.Model):
    author_name = models.CharField(max_length=100)
    post_type = models.CharField(max_length=100)
    post_title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    time = models.TimeField(auto_now_add=True)
    img = models.ImageField(upload_to='userimages/',blank=True)
    view_count = models.IntegerField(blank=True,null=True)
    like = models.ManyToManyField(User,related_name='postlikes',default=True,blank=True)
    bookmarks = models.ManyToManyField(User,related_name='bookmarks',default=True,blank=True)

    def __str__(self):
        return self.author_name
    
    def number_of_likes(self):
        return self.like.count()
    

class comment(models.Model):
    Content = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=80)
    Email = models.EmailField()
    post = models.ForeignKey(author,related_name='add_posts', on_delete=models.CASCADE)
    Author = models.CharField(max_length=120)
    parent = models.ForeignKey('self',on_delete =models.CASCADE,blank = True,null=True,related_name='replies')


    def _str_(self):
        return self.Name
class subscribe(models.Model):
    email = models.EmailField()
    time = models.DateTimeField(auto_now_add=True)   

