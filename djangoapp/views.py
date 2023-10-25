from django.shortcuts import render
from .models import Candidate,Education
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'form.html')

def addeducation(request):
    success = False
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        dict=zip(
            request.POST.getlist('course'),
            request.POST.getlist('university'),
            request.POST.getlist('year'),
        )
        data_dict=[{'course':course,
                    'university':university,
                    'year':year,}
                    for course,university,year in dict]
        print(data_dict)
        print(name)
        print(email)
        if Candidate.objects.filter(email=email).exists():
             return HttpResponse("duplicate Email found", status=400)
        add=Candidate(name=name,email=email)
        add.save()
        r_id=add.id
        for i in data_dict:
            course = i.get('course')
            university = i.get('university')
            year = i.get('year')
            candidate_instance = Candidate.objects.get(id=r_id)

            data1=Education(reg_id=candidate_instance,course=course,university=university,year=year)
            data1.save()
        success = True   
    return render(request,'form.html',{'success': success})

