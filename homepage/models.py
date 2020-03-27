from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    aboutme = models.CharField(max_length=100)
    dob = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phonenum = models.CharField(max_length=20)
    cvlink = models.CharField(max_length=100)
    linkedinlink = models.CharField(max_length=100)
    profileimage = CloudinaryField('image')

class Education(models.Model):
    edname = models.CharField(max_length=20)
    eddate = models.CharField(max_length=20)
    eddetail = models.CharField(max_length=100)
    eduid = models.ForeignKey(User,on_delete=models.CASCADE)

class Skills(models.Model):
    skill1 = models.CharField(max_length=20)
    skill2 = models.CharField(max_length=20)
    skill3 = models.CharField(max_length=20)
    sduid = models.ForeignKey(User,on_delete=models.CASCADE)


class Experience(models.Model):
    ename = models.CharField(max_length=20)
    edate = models.CharField(max_length=20)
    edetail = models.CharField(max_length=100)
    euid = models.ForeignKey(User,on_delete=models.CASCADE)

class Achievement(models.Model):
    aname = models.CharField(max_length=20)
    adate = models.CharField(max_length=20)
    adetail = models.CharField(max_length=100)
    auid = models.ForeignKey(User,on_delete=models.CASCADE)

class Projects(models.Model):
    pname = models.CharField(max_length=20)
    pdate = models.CharField(max_length=20)
    pdetail = models.CharField(max_length=100)
    image = CloudinaryField('image')
    puid = models.ForeignKey(User,on_delete=models.CASCADE)
