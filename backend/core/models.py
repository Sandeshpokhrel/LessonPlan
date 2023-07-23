from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#user
class User(AbstractUser):
  email = models.EmailField(unique=True)

#subject
class Subject(models.Model):
  sub_name = models.CharField(max_length=225)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

#section and year
class SectionYear(models.Model):
  section = models.CharField(max_length=255)
  year = models.CharField(max_length=255)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

#plan
class Plan(models.Model):
  plan_name = models.CharField(max_length=255)
  section_year = models.ForeignKey(SectionYear, on_delete=models.CASCADE)

#chapter
class Chapter(models.Model):
  chapter_name = models.CharField(max_length=255)
  plan = models.OneToOneField(Plan, on_delete=models.PROTECT)

#assignment
class Assingnment(models.Model):
  assign_name = models.CharField(max_length=255)
  updated_date = models.DateField(auto_now=True)
  chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

#assignment file
class AssignmentFile(models.Model):
  assignment = models.OneToOneField(Assingnment, on_delete=models.CASCADE, 
                               related_name='files')
  file = models.FileField(upload_to='core/assignment/files')

#resource
class Resource(models.Model):
  res_name = models.CharField(max_length=255)
  updated_date = models.DateField(auto_now=True)
  chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

#resource file
class ResourceFile(models.Model):
  resource = models.OneToOneField(Resource, on_delete=models.CASCADE, 
                               related_name='files')
  file = models.FileField(upload_to='core/resource/files')