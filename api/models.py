from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=4,  decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="media/images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')