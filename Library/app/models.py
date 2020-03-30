from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone=models.PositiveIntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    picture=models.ImageField(upload_to="profile",default="none.jpg",blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.username


types=[
        ('political','political'),('social','social'),('engineering','engineering'),('computer','computer'),('biological','biological'),('reaerch','research')
    ]
class Book(models.Model):
    code=models.CharField(max_length=20,unique=True,blank=False)
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    publisher=models.CharField(max_length=20)
    type=models.CharField(max_length=20,choices=types,default='computer')
    issued=models.BooleanField(default=False)
    issue_date=models.DateTimeField(blank=True,null=True,default=None)
    due_date=models.DateTimeField(blank=True,null=True,default=None)
    slug=models.SlugField(unique=True,max_length=100)
    def __str__(self):
        return str(self.name)
    
