# jobs/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class JobModel(models.Model):
    Job_region = models.CharField(max_length=50)

class UserModel(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class JobPost(models.Model):
    # Job Details
    email = models.EmailField()
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_region = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')])
    job_description = models.TextField()
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)

    # Company Details
    company_name = models.CharField(max_length=100)
    company_tagline = models.CharField(max_length=255, blank=True)
    company_description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.job_title
    
class FeedModel(models.Model):
    firstnames = models.CharField(max_length=50)
    lastnames = models.CharField(max_length=50)
    emails = models.CharField(max_length=50)
    subjects= models.CharField(max_length=50)
    messages = models.CharField(max_length=50)


    def __str__(self):
        return self.subjects
    
    
class CommentModel(models.Model):
    Image = models.ImageField(upload_to='comment_images/', default='comment_images/default.jpg',null=True)  # <- fixed image
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name