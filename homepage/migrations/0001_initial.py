# Generated by Django 3.0.4 on 2020-03-27 11:58

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('aboutme', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phonenum', models.CharField(max_length=20)),
                ('cvlink', models.CharField(max_length=100)),
                ('linkedinlink', models.CharField(max_length=100)),
                ('profileimage', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(max_length=20)),
                ('skill2', models.CharField(max_length=20)),
                ('skill3', models.CharField(max_length=20)),
                ('sduid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.User')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('pdate', models.CharField(max_length=20)),
                ('pdetail', models.CharField(max_length=100)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('puid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.User')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=20)),
                ('edate', models.CharField(max_length=20)),
                ('edetail', models.CharField(max_length=100)),
                ('euid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.User')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edname', models.CharField(max_length=20)),
                ('eddate', models.CharField(max_length=20)),
                ('eddetail', models.CharField(max_length=100)),
                ('eduid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.User')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=20)),
                ('adate', models.CharField(max_length=20)),
                ('adetail', models.CharField(max_length=100)),
                ('auid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.User')),
            ],
        ),
    ]
