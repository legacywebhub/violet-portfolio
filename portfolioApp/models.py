from enum import unique
from django.db import models
from ckeditor.fields import RichTextField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.
class WebsiteSetting(models.Model):
    title = models.CharField(max_length=40, blank=False)
    meta_keywords = models.CharField(max_length=200, blank=False)
    meta_description = models.TextField(max_length=160, blank=False)
    logo = models.ImageField(upload_to="images", blank=True, null=True)
    header = models.CharField(max_length=50, blank=True, null=True)
    google_analytics = models.TextField(max_length=1500, blank=True, null=True) 

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id and WebsiteSetting.objects.exists():
            raise ValueError('This model can only have one setting which can be edited')
        else:
            super().save( *args, **kwargs)


class Info(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    age = models.PositiveIntegerField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=False)
    profession = models.CharField(max_length=30,blank=False)
    my_image = models.ImageField(upload_to="images/about", blank=True, null=True)
    about_me = models.TextField(max_length=500, blank=False)
    about_services = models.TextField(max_length=2000, blank=True, null=True)
    about_team = models.TextField(max_length=1000, blank=True, null=True)
    CV = models.FileField(upload_to="documents", blank=True, null=True, storage=RawMediaCloudinaryStorage())
    address = models.CharField(max_length=150, blank=False)
    email_1 = models.EmailField(blank=False)
    email_2 = models.EmailField(blank=True, null=True)
    phone_1 = models.CharField(max_length=20, blank=False) 
    phone_2 = models.CharField(max_length=20, blank=True, null=True)
    phone_3 = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_link = models.URLField(max_length=300, blank=True, null=True)
    facebook_link = models.URLField(max_length=300, blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True, null=True)
    instagram_link = models.URLField(max_length=300, blank=True, null=True)
    tiktok_link = models.URLField(max_length=300, blank=True, null=True)
    linkedin_link = models.URLField(max_length=300, blank=True, null=True)
    youtube_link = models.URLField(max_length=300, blank=True, null=True)
    pin_interest_link = models.URLField(max_length=300, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.id and Info.objects.exists():
            raise ValueError('This model can only have one setting which can be edited')
        else:
            super().save( *args, **kwargs)
    

class Skill(models.Model):
    skill = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.skill


class Service(models.Model):
    service = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to="images/services",blank=True, null=True)
    detail = models.TextField(max_length=500, blank=False)
    
    def __str__(self):
        return self.service

class Team(models.Model):
    name = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to="images/team", blank=False)
    role = models.CharField(max_length=50, blank=False)
    skill1 = models.CharField(max_length=25, blank=True, null=True)
    skill2 = models.CharField(max_length=25, blank=True, null=True)
    skill3 = models.CharField(max_length=25, blank=True, null=True)
    whatsapp_link = models.URLField(max_length=300, blank=True, null=True)
    facebook_link = models.URLField(max_length=300, blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True, null=True)
    instagram_link = models.URLField(max_length=300, blank=True, null=True)


class PortfolioCategory(models.Model):
    categories = (
        ('web-design', 'web design'),
        ('web-development', 'web development'),
        ('graphic-design', 'graphic design'),
        ('product', 'product'),
        ('service', 'service'),
        ('book', 'book')
    )
    category = models.CharField(max_length=25, choices=categories, default='graphic-design', unique=True)

    def __str__(self):
        return self.category


class Portfolio(models.Model):
    name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.PROTECT, blank=False)
    author = models.CharField(max_length=25, blank=True, null=True)
    image = models.ImageField(upload_to="images/portfolios", blank=False)
    detail = models.TextField(max_length=1500, blank=True, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100, blank=False, null=False)
    client_image = models.ImageField(upload_to='images/testimonials', blank=False)
    service = models.CharField(max_length=50, blank=False)
    testimony = models.CharField(max_length=3000, blank=False, null=False)
    company = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    website_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.client_name
    
class Content(models.Model):
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=150, blank=False)
    image = models.ImageField(upload_to='images/contents', blank=True, null=True)
    image_url = models.CharField(max_length=2500, blank=True, null=True)
    content = RichTextField(max_length=20000, blank=False, null=False)
    quote = models.CharField(max_length=250, blank=True, null=True)
    ad = models.TextField(max_length=2000, blank=True, null=True)
    
    def get_absolute_url(self):
        return f'/content/{self.id}/'


class Message(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone = models.PositiveIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=10000, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    