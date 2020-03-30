from django.shortcuts import render
from homepage.forms import UserForm,EducationForm,ExperienceForm,AchievementForm,ProjectsForm,SkillForm
from django.forms import formset_factory

from .models import User,Education,Experience,Projects,Achievement,Skills



# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def portfolio(request):
    usrnamefromPath = request.get_full_path()[4:]
    user = User.objects.filter(username=usrnamefromPath)

    if len(user)>0:
        user = User.objects.get(username=usrnamefromPath)
        educations = Education.objects.filter(eduid__username=user.username)
        experiences = Experience.objects.filter(euid__username=user.username)
        projects = Projects.objects.filter(puid__username=user.username)
        achievements = Achievement.objects.filter(auid__username=user.username)
        skills = Skills.objects.get(suid__username=user.username)

        

        return render(request,'index.html',{'user':user,
        'experiences':experiences,
        'educations':educations,
        'projects':projects,
        'achievements':achievements,
        'skills':skills})
    else:
        return render(request,'404.html')

def register(request):
    if request.method == "POST":
        print(request.POST["name"])
        return render(request,'index.html',{'name':'Abhay Nigam'})
    else:
        userform = UserForm()
        educationformhigh = EducationForm(prefix="educationformhigh")
        educationformintermediate = EducationForm(prefix="educationformintermediate")
        educationformcollege = EducationForm(prefix="educationformcollege")

        experienceform1 =ExperienceForm(prefix="experienceform1")
        experienceform2 =ExperienceForm(prefix="experienceform1")
        experienceform3 =ExperienceForm(prefix="experienceform1")

        achievementForm1 = AchievementForm(prefix="achievementForm1")
        achievementForm2 = AchievementForm(prefix="achievementForm2")
        achievementForm3 = AchievementForm(prefix="achievementForm3")

        projectsForm1 = ProjectsForm(prefix="projectsForm1")
        projectsForm2 = ProjectsForm(prefix="projectsForm2")
        projectsForm3 = ProjectsForm(prefix="projectsForm3")
        
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
        return render(request,'afterregister.html',{'username':'abhay'})

def portfolioCreated(request):
    if request.method == 'POST':
        user = UserForm(request.POST,request.FILES)
        educationformhigh = EducationForm(request.POST,request.FILES,prefix="educationformhigh")
        experienceform1 =ExperienceForm(request.POST,request.FILES,prefix="experienceform1")
        educationformintermediate = EducationForm(request.POST,request.FILES,prefix="educationformintermediate")
        educationformcollege = EducationForm(request.POST,request.FILES,prefix="educationformcollege")

        experienceform2 =ExperienceForm(request.POST,request.FILES,prefix="experienceform1")
        experienceform3 =ExperienceForm(request.POST,request.FILES,prefix="experienceform1")

        achievementForm1 = AchievementForm(request.POST,request.FILES,prefix="achievementForm1")
        achievementForm2 = AchievementForm(request.POST,request.FILES,prefix="achievementForm2")
        achievementForm3 = AchievementForm(request.POST,request.FILES,prefix="achievementForm3")

        projectsForm1 = ProjectsForm(request.POST,request.FILES,prefix="projectsForm1")
        projectsForm2 = ProjectsForm(request.POST,request.FILES,prefix="projectsForm2")
        projectsForm3 = ProjectsForm(request.POST,request.FILES,prefix="projectsForm3")

        skillsform = SkillForm(request.POST,request.FILES)

        usrname =''
        #saving
        if user.is_valid():
            usrname = user.cleaned_data['username']
            existinguser = User.objects.filter(username=usrname)

        if len(existinguser)==0:
                
            if user.is_valid() and educationformhigh.is_valid() and educationformintermediate.is_valid() and educationformcollege.is_valid() and experienceform1.is_valid() and experienceform2.is_valid() and experienceform3.is_valid() and achievementForm1.is_valid() and achievementForm2.is_valid() and projectsForm1.is_valid() and projectsForm2.is_valid() and projectsForm3.is_valid() and skillsform.is_valid():

                user = user.save()
                print(user)

                instance = educationformhigh.save(commit=False)
                instance.eduid = user
                instance.save()

                instance = educationformintermediate.save(commit=False)
                instance.eduid = user
                instance.save()

                instance = educationformcollege.save(commit=False)
                instance.eduid = user
                instance.save()

                instance = experienceform1.save(commit=False)
                instance.euid = user
                instance.save()

                instance = experienceform2.save(commit=False)
                instance.euid = user
                instance.save()

                instance = experienceform3.save(commit=False)
                instance.euid = user
                instance.save()

                instance = achievementForm1.save(commit=False)
                instance.auid = user
                instance.save()

                instance = achievementForm2.save(commit=False)
                instance.auid = user
                instance.save()

                instance = achievementForm3.save(commit=False)
                instance.auid = user
                instance.save()

                instance = projectsForm1.save(commit=False)
                instance.puid = user
                instance.save()

                instance = projectsForm2.save(commit=False)
                instance.puid = user
                instance.save()

                instance = projectsForm3.save(commit=False)
                instance.puid = user
                instance.save()

                instance = skillsform.save(commit=False)
                instance.suid = user
                instance.save()
                return render(request,'afterregister.html',{'username':usrname})
            else:
                print(user.is_valid())
                print("-----")
                print(user.errors)
        else:
            return render(request,'single.html',{'name':'Abhay Nigam','userform':user,'educationformhigh':educationformhigh,
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
            ,'error':'Username Exists Try Something more Unique'
            })
    return render(request,'index.html')