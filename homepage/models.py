from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    aboutme = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    pincode = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phonenum = models.CharField(max_length=50)
    cvlink = models.CharField(max_length=100)
    linkedinlink = models.CharField(max_length=100)
    profileimage = CloudinaryField('image')


class Education(models.Model):
    edname = models.CharField(max_length=50)
    edorgname = models.CharField(max_length=50)
    eddate = models.CharField(max_length=50)
    eddetails = models.CharField(max_length=50)
    eduid = models.ForeignKey(User,on_delete=models.CASCADE)

class Skills(models.Model):
    skill1 = models.CharField(max_length=50)
    skill2 = models.CharField(max_length=50)
    skill3 = models.CharField(max_length=50)
    suid = models.ForeignKey(User,on_delete=models.CASCADE)


class Experience(models.Model):
    ename = models.CharField(max_length=50)
    eorgname = models.CharField(max_length=50)
    edate = models.CharField(max_length=50)
    edetail = models.CharField(max_length=150)
    euid = models.ForeignKey(User,on_delete=models.CASCADE)

class Achievement(models.Model):
    aname = models.CharField(max_length=50)
    aorgname = models.CharField(max_length=50)
    adate = models.CharField(max_length=50)
    adetail = models.CharField(max_length=150)
    auid = models.ForeignKey(User,on_delete=models.CASCADE)

class Projects(models.Model):
    pname = models.CharField(max_length=50)
    purl = models.CharField(max_length=50)
    pdetail = models.CharField(max_length=150)
    image = CloudinaryField('image')
    puid = models.ForeignKey(User,on_delete=models.CASCADE)
