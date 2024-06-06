from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    phone = models.CharField(max_length=15, blank=True)
    place = models.CharField(max_length=255, blank=True)
    nickname = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def __str__(self):
        return self.username



class Package(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    about = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField()
    location = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    no_of_people = models.CharField(max_length=50)
    hotel = models.ImageField(upload_to='package_photos/', blank=True, null=True)
    destination = models.ImageField(upload_to='package_photos/', blank=True, null=True)
    activity = models.ImageField(upload_to='package_photos/', blank=True, null=True)
    attraction = models.ImageField(upload_to='package_photos/', blank=True, null=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)
   
    def __str__(self):
        return self.comment


class Blogs(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    food = models.ImageField(upload_to='blog_photos/', blank=True, null=True)
    hotel = models.ImageField(upload_to='blog_photos/', blank=True, null=True)
    travelling = models.ImageField(upload_to='blog_photos/', blank=True, null=True)
    activity = models.ImageField(upload_to='blog_photos/', blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    review = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.review
