from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# # Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home') 

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=200, blank=True, null=True)
    fb_url = models.CharField(max_length=200, blank=True, null=True)
    instagram_url = models.CharField(max_length=200, blank=True, null=True)
    pinterest_url = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("home")
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(blank=True, null=True, upload_to='images/')
    title_tag = models.CharField(max_length=50,null=True,blank=True)
    content = RichTextField(blank=True,null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=200, default="nocategory")
    likes = models.ManyToManyField(User,related_name = 'blog_posts')
    snippet = models.CharField(max_length=50 ,null=True, blank = True )
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post = models.ForeignKey(Post ,related_name="comments" ,on_delete=models.CASCADE)
    name = models.CharField (max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)
