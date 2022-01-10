from django.db import models
from .utils import create_shortened_url

#Importing the user model 
from django.contrib.auth.models import User
# Create your models here.

# Profile model
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.FloatField(default='', null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    image =  models.ImageField(default='default.jpg', upload_to="profile_pics")
    bio = models.CharField(max_length=100, null=True, blank=True, help_text="Bio must be 100 characters long")

    class Meta:
        ordering = ['last_name']


    def __str__(self):
        """String for representing the Model Object."""
        return f'{self.last_name}, {self.first_name}'




class ShortenerModel(models.Model):
    '''
    Creates a short url based on the long one
    
    created -> Hour and date a shortener was created 
    
    times_followed -> Times the shortened link has been followed

    long_url -> The original link

    short_url ->  shortened link https://domain/(short_url)
    ''' 
    created = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)    

    long_url = models.URLField()

    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:

        ordering = ["-created"]


    def __str__(self):

        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):

        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)