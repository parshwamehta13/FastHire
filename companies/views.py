from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from companies.models import Company,Resume,Recruiter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.

def listCompanies(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	recruiter_profile = Recruiter.objects.get(recruiter=request.user)
	profile_code = recruiter_profile.recruiter_profile_code
	company_list = Company.objects.filter(profile_code=profile_code)
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		company_list = company_list.filter(name__icontains=q)
	location = []
	newList = []

	l = company_list.values('location').distinct()
	location_list = []
	for i in l:
		location_list.append(i['location'])

	for i in location_list:
		if str(i) in request.GET:
			location.append(str(i))
	storage = get_messages(request)
	if len(location)!=0:
		for i in companyList:
			if i.location in location:
				newList.append(i)
		t = get_template('database.html')
		html = t.render(Context({'company_list':newList,'location_list':location_list,'user':request.user,'messages_list':storage}))
		return HttpResponse(html)
	else:
		t = get_template('database.html')
		html = t.render(Context({'location_list':location_list,'company_list':company_list,'user':request.user,'messages_list':storage}))
		return HttpResponse(html)	

# def companyProfile(request,company_id):
# 	if not request.user.is_authenticated():
# 		return HttpResponseRedirect('/')
	
# 	# if request.method == 'POST':
# 	# 	company = Company.objects.filter(id=company_id)
# 	# 	position_applied = company[0].job_title
# 	# 	recruiter = request.user.id
# 	# 	name = request.POST["name_applicant"]
# 	# 	email = request.POST["email_applicant"]
# 	# 	mobile = request.POST["mobile_applicant"]
# 	# 	current_company = request.POST["current_applicant_company"]
# 	# 	current_salary = request.POST["current_applicant_salary"]
# 	# 	cv = request.POST["cv_applicant"]
# 	# 	temp = Resume(name_applicant=name,current_company=current_company,current_salary=current_salary,emailid=email,mobile=mobile,resume=cv,company_applied=company[0],position_applied=position_applied,recruiter_id=recruiter)
# 	# 	temp.save()
# 	# 	messages.success(request, 'Resume of candidate uploaded')
# 	# 	return HttpResponseRedirect('/company/')
# 	else:
# 		companyObject = Company.objects.filter(id=company_id)
# 		t = get_template('companyProfile.html')
# 		html = t.render(Context({'item':companyObject[0]}))
# 		return HttpResponse(html)

def recruiterPanel (request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	resumeList = Resume.objects.filter(recruiter_id=request.user.id)
	t = get_template('recruiterPanel.html')
	html = t.render(Context({'resumeList':resumeList,'user':request.user}))
	return HttpResponse(html)

def apply(request, company_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	elif request.method == 'POST':
		company = Company.objects.filter(id=company_id)
		position_applied = company[0].job_title
		recruiter = request.user.id
		name = request.POST["name_applicant"]
		email = request.POST["email_applicant"]
		mobile = request.POST["mobile_applicant"]
		current_company = request.POST["current_applicant_company"]
		current_salary = request.POST["current_applicant_salary"]
		cv = request.POST["cv_applicant"]
		temp = Resume(name_applicant=name,current_company=current_company,current_salary=current_salary,emailid=email,mobile=mobile,resume=cv,company_applied=company[0],position_applied=position_applied,recruiter_id=recruiter)
		temp.save()
		messages.success(request, 'Resume of candidate uploaded')
		return HttpResponseRedirect('/company/')
	else:
		companyObject = Company.objects.filter(id=company_id)
		return render(request,'apply.html',{'item':companyObject[0]})
