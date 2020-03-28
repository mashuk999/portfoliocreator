from django.contrib import admin

# Register your models here.
from .models import User,Education,Experience,Projects,Achievement,Skills

admin.site.register(User)

admin.site.register(Education)

admin.site.register(Experience)

admin.site.register(Projects)

admin.site.register(Achievement)

admin.site.register(Skills)