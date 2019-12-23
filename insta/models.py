from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='images/')
    bio=models.CharField(max_length=100)

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=100)
    profile=models.ForeignKey(Profile)
    likes=models.IntegerField()
    comments=models.CharField(max_length=100)
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


