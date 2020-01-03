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
    
class Image(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=100)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    # comments=models.ForeignKey(Comments,null=True)
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

    @classmethod
    def get_image_id(cls,imageId):
        '''
        function that gets an image id    
        '''
        image_id=cls.objects.filter(id=imageId)
        return image_id

    @classmethod
    def single_image(cls,image_id):
        '''
        function gets a single image posted by id
        '''
        image_posted=cls.objects.get(id=image_id)
        return image_posted

class Comments(models.Model):
    detail= HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    image_foreign=models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.detail

    @classmethod
    def get_comments(cls):
        comment=cls.objects.all()
        return comment

    @classmethod
    def get_singlepost_comments(cls, id):
        '''
        function that gets comments for a single post
        '''
        comments=cls.objects.filter(image_foreign__in=id)
        return comments
    def save_comment(self):
        '''
        function that saves a new comment
        '''
        self.save()

    def delete_comment(self):
        '''
        function that deletes a comment
        '''
        self.delete()

    # @classmethod
    # def update_caption(cls,comment_id, text):
    #     '''
    #     function that updates a comment
    #     '''
    #     searched=cls.objects.get(id=comment_id)
    #     searched.body=text
    #     searched.save()
    #     return searched
    






        
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()


