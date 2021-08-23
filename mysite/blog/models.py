from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.timezone import now

# Create your models here.

class BlogPosts(models.Model):

    sno = models.AutoField(primary_key=True)
    blog_title = models.TextField(max_length=50)
    blog_content = models.TextField(max_length=5000)
    blog_author = models.CharField(max_length=50)
    blog_date = models.DateTimeField(blank=True)

    def __str__(self):

        return self.blog_title

class BlogComments(models.Model):
    sno = models.AutoField(primary_key=True)
    comments = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPosts, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)


    def __str__(self):

        return str(self.sno)






