from django.db import models
from datetime import datetime

class Post(models.Model):
    fullname = models.CharField(max_length=50)
    dateofbarth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=150)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    username = models.CharField(max_length=150,unique=True,null=False,blank=False)  # New field
    password = models.CharField(max_length=128,null=False,blank=False)  # New field

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
