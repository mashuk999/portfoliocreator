from django import forms

from .models import User,Education,Experience,Projects,Achievement,Skills,Temp

# Next two lines are only used for generating the upload preset sample name
from cloudinary.compat import to_bytes
import cloudinary, hashlib

class UserForm(forms.ModelForm):

    class Meta:
            model = User
            fields = [
                'username',
                 'title',
                 'name',
                 'dob',
                 'address',
                 'pincode',
                 'email',
                 'phonenum',
                 'cvlink',
                 'aboutme',
                 'linkedinlink',
                 'image'
                 ]
            labels ={
                'username':'username (will be used to generate URL)',
                'dob':'Date Of Birth',
            }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education

        fields = [
            'edname',
            'eddate',
            'eddetail',
        ]

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience

        fields=[
            'ename',
            'edate',
            'edetail'
        ]

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement

        fields=[
            'aname',
            'adate',
            'adetail'
        ]

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects

        fields=[
            'pname',
            'pdate',
            'pdetail',
            'image'
        ]

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills

        fields=[
            'skill1',
            'skill2',
            'skill3',
        ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Temp
        fields = '__all__'