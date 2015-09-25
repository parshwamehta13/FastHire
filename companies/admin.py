from django.contrib import admin

# Register your models here.

from .models import Company,Resume,Recruiter

admin.site.register(Company)
admin.site.register(Resume)
admin.site.register(Recruiter)
