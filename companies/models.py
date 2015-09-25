from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
	name = models.CharField(max_length=30,default='DEFAULT VALUE')
	job_title = models.CharField(max_length=30,default='DEFAULT VALUE')
	work_exp = models.CharField(max_length=200,default='DEFAULT VALUE')
	job_profile = models.CharField(max_length=1000,default='DEFAULT VALUE')
	job_requirements = models.CharField(max_length=1000,default='DEFAULT VALUE')
	location = models.CharField(max_length=60,default='DEFAULT VALUE')
	vacancies = models.IntegerField(default=0)
	salary = models.IntegerField(default=0)
	profile_code = models.IntegerField(default=0)

	
	def __unicode__(self):
		return self.name

class Resume (models.Model):
	name_applicant = models.CharField(max_length=30,default='DEFAULT VALUE')
	current_company = models.CharField(max_length=30,default='DEFAULT VALUE')
	current_salary = models.CharField(max_length=10,default='DEFAUL')
	emailid = models.EmailField (max_length=30,default='DEFAULT VALUE')
	mobile = models.IntegerField(default=0)
	resume = models.CharField(max_length=30,default='DEFAULT VALUE')
	company_applied = models.ForeignKey('Company')
	position_applied = models.CharField(max_length=30,default='DEFAULT VALUE')
	recruiter_id = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name_applicant

class Recruiter (models.Model):
	recruiter = models.OneToOneField(User)
	recruiter_profile_code = models.IntegerField(default=0)

	def __unicode__(self):
		return self.recruiter.username
