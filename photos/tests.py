from django.test import TestCase
from .models import Profile,Image,tags
import datetime as dt
# Create your tests here.

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Profile(first_name = 'Umutoni', last_name ='Jacqueline', email ='jacquelineumutoni@gmail.com')

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.wecode= Profile(first_name = 'Umutoni', last_name ='Jacqueline', email ='jacquelineumutoni@gmail.com')
        self.wecode.save_profile()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()                        

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',profile = self.wecode)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Profile.objects.all().delete()  
        tags.objects.all().delete()
        Image.objects.all().delete()

    
    
    