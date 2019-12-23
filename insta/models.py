from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='images/',blank=True)
    bio=models.CharField(max_length=100)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    @classmethod
    def get_profile(cls):
        profile=cls.objects.all()
        return profile

class Comments(models.Model):
    detail= HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

    @classmethod
    def get_comments(cls):
        comment=cls.objects.all()
        return comment

    
class Image(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=100)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)
    likes=models.IntegerField(null=True)
    comments=models.ForeignKey(Comments,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    
    @classmethod
    def get_images(cls):
        image=cls.objects.all()
        return image
    @classmethod
    def search_by_category(cls,category):
        category_result=cls.objects.filter(image_name__icontains=category)
        return category_result
        
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


