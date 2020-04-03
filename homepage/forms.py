from django import forms

from .models import User,Education,Experience,Projects,Achievement,Skills

# Next two lines are only used for generating the upload preset sample name
from cloudinary.compat import to_bytes
import cloudinary, hashlib

class UserForm(forms.ModelForm):

    class Meta:
            model = User
            fields = '__all__'
            labels ={
                'username':'Username (must be unique)',
                'dob':'Date Of Birth',
                'aboutme':'About me',
                'phonenum':'Contact Number',
                'cvlink':'CV Link',
                'linkedinlink':'LinkedIN Profile',
                'profileimage':'Profile Picture'
            }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude =['eduid']

        labels = {
            'edname':'Name of the Class/College/University',
            'edorgname':'Organisation Name',
            'eddate':'Duration Year',
            'eddetails':'Any Other Activity ',
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience

        fields='__all__'
        exclude =['euid']
        labels = {
            'ename':'Your Experience Towards',
            'eorgname':'Organisation Name',
            'edate':'Duration For Achieving Experience',
            'edetail':'Description',
        }

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement

        fields='__all__'
        exclude =['auid']
        labels = {
            'aname':"Your Achievements",
            'aorgname':"Achievement's Organisation Name",
            'adate':'Date/Duration',
            'adetail':'Description',
        }

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects

        fields='__all__'
        exclude =['puid']
        labels = {
            'pname':'Name of the Project',
            'pdate':'Time Taken To Build The Project',
            'pdetail':'Description',
            'purl':'Project Link',
            'image':'Project Screenshot'
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills

        fields='__all__'
        exclude =['suid']
        labels = {
            'skill1':'Name of the Skill 1',
            'skill2':'Name of the Skill 2',
            'skill3':'Name of the Skill 3',

        }
        