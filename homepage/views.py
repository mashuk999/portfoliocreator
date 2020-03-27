from django.shortcuts import render
from homepage.forms import UserForm,EducationForm,ExperienceForm,AchievementForm,ProjectsForm,SkillForm



# Create your views here.
def homepage(request):
    print(request.get_full_path())
    return render(request,'index.html',{'name':request.get_full_path()[4:]})

def register(request):
    if request.method == "POST":
        print(request.POST["name"])
        return render(request,'index.html',{'name':'Abhay Nigam'})
    else:
        userform = UserForm()
        educationformhigh = EducationForm()
        educationformintermediate = EducationForm()
        educationformcollege = EducationForm()

        experienceform1 =ExperienceForm()
        experienceform2 =ExperienceForm()
        experienceform3 =ExperienceForm()

        achievementForm1 = AchievementForm()
        achievementForm2 = AchievementForm()
        achievementForm3 = AchievementForm()

        projectsForm1 = ProjectsForm()
        projectsForm2 = ProjectsForm()
        projectsForm3 = ProjectsForm()
        
        skillsform = SkillForm()

        print(request.get_full_path())
        return render(request,'single.html',{'name':'Abhay Nigam','userform':userform,'educationformhigh':educationformhigh,
        'educationformintermediate':educationformintermediate
        ,'educationformcollege':educationformcollege
        ,'experienceform1':experienceform1
        ,'experienceform2':experienceform2
        ,'experienceform3':experienceform3
        ,'achievementform1':achievementForm1
        ,'achievementform2':achievementForm2
        ,'achievementform3':achievementForm3
        ,'projectsform1':projectsForm1
        ,'projectsform2':projectsForm2
        ,'projectsform3':projectsForm3
        ,'skillsform':skillsform
        })

def temp(request):
    if request.method=='POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('good')
            return render(request,'single.html')
        return render(request,'index.html')
    else:
        photoform = PhotoForm()
        return render(request,'temp.html',{'photoform':photoform})
