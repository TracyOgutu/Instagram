from django.test import TestCase
from .models import Profile,Image,Comments,NewsLetterRecipients
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        creating a foreign key instance
        '''
        self.newuser=User(username='sandy')
        self.newuser.save()

        self.biography=Profile(profile_photo='pic.jpg',bio='treats',editor=self.newuser)

    def test_instance(self):
        '''
        Testing the self instance
        '''
        self.assertTrue(isinstance(self.biography,Profile))

    def test_save_profile(self):
        '''
        Testing save profile function
        '''
        self.biography.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_profile(self):
        '''
        Testing delete profile function
        '''
        self.biography.save_profile()
        self.biography.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    def test_get_profile(self):
        '''
        Testing profile retrieval
        '''
        self.biography.save_profile()
        firstprofile=Profile.get_profile()
        self.assertTrue(firstprofile is not None)


class ImageTestClass(TestCase):

    def setUp(self):
        '''
        creating a user foreign key instance
        '''
        self.newuser=User(username='sandy') 
        '''
        saving the foreign key instance
        '''
        self.newuser.save()

        '''
        creating the Image class instance and including foreign key references
        '''

        self.images=Image(image='img.jpg',image_name='building',image_caption='whatamarvel',editor=self.newuser)

    def test_instance(self):
        '''
        Testing the Image instance
        '''
        self.assertTrue(isinstance(self.images,Image))

    def test_save_image(self):
        '''
        Testing the save image function
        '''
        self.images.save_image()
        allimages=Image.objects.all()
        self.assertTrue(len(allimages)>0)

    def test_delete_image(self):
        '''
        Testing the delete image function
        '''
        self.images.save_image()
        self.images.delete_image()
        allimages=Image.objects.all()
        self.assertTrue(len(allimages)==0)

    def test_get_images(self):
        '''
        Testing image retrieval
        '''
        self.images.save_image()
        secondimage=Image.get_images()
        self.assertTrue(secondimage is not None)

class CommentsTestClass(TestCase):

    def setUp(self):
        '''
        creating a user foreign key instance
        '''
        self.newuser=User(username='sandy')
        self.newuser.save()
        '''
        creating an image instance to be used as a foreign key for the image_foreign field in Comments Class
        '''

        self.imageid=Image(id='1',image='img.jpg',image_name='building',image_caption='whatamarvel',editor=self.newuser)
        self.imageid.save()

        '''
        Creating the Comments class instance
        '''

        self.newcomment=Comments(detail='thisisacomment',editor=self.newuser,image_foreign=self.imageid)

    def test_instance(self):
        '''
        Testing the Comments class instance
        '''
        self.assertTrue(isinstance(self.newcomment,Comments))
    
    def test_save_comment(self):
        '''
        Testing the save comment function
        '''
        self.newcomment.save_comment()
        allcomments=Comments.objects.all()
        self.assertTrue(len(allcomments)>0)

    def test_delete_comment(self):
        '''
        Testing the delete comments function
        '''
        self.newcomment.save_comment()
        self.newcomment.delete_comment()
        allcomments=Comments.objects.all()
        self.assertTrue(len(allcomments)==0)

    def test_get_comments(self):
        '''
        Testing comment retrieval
        '''
        self.newcomment.save_comment()
        commentone=Comments.get_comments()
        self.assertTrue(commentone is not None)



    



