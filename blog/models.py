from django.db import models

# Create your models here.
class Blog(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)
    genre=models.CharField(max_length=50,default="")
    content= models.TextField()
    short_desc=models.CharField(max_length=250,default="")
    slug=models.CharField(max_length=300)
    time=models.DateTimeField(auto_now_add=True)
    poster=models.CharField(max_length=250,default="")
  
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
