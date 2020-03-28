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
                'username':'username (will be used to generate URL)',
                'dob':'Date Of Birth',
            }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude =['eduid']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience

        fields='__all__'
        exclude =['euid']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement

        fields='__all__'
        exclude =['auid']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects

        fields='__all__'
        exclude =['puid']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills

        fields='__all__'
        exclude =['suid']