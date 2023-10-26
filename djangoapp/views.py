from django.shortcuts import render,redirect
from .models import Candidate,Education
from django.http import HttpResponse
from django.http import JsonResponse

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


def alluser(request):
    users=Candidate.objects.all()
    # for i in users:
    #    name= i.name
    #    print(name)
    context={'user':users}
    #    return HttpResponse("ok", status=200)
    return render(request,'alluser.html',context)


def editData(request,id):
    userdata=Candidate.objects.get(id=id)
    ed_data=Education.objects.filter(reg_id=userdata).all()
    context={'userdata':userdata}
    context2={'ed_data':ed_data}
    print(ed_data.values_list())
    print(ed_data.values())
    print(userdata)
    print(userdata.name)
    print(userdata.email)
    # return HttpResponse("ok", status=200)
    return render(request,'edit.html',locals())

def updateData(request,id):
    success = False

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        print(name)
        print(email)
        # Candidate.objects.filter(id=id).update(name=name,email=email)
        add=Candidate.objects.get(id=id)
        add.name=name
        add.email=email             
        add.save()
        dict=zip(
            request.POST.getlist('course'),
            request.POST.getlist('university'),
            request.POST.getlist('year'),
        )
        print(dict)
        dict_data=[{
            'course':course,
            'university':university,
            'year':year,
        } for course,university,year in dict]
        print(dict_data)
        Education.objects.filter(reg_id=id).delete()
        for data in dict_data:
            course = data.get('course')
            university = data.get('university')
            year = data.get('year')
            candidate_instance = Candidate.objects.get(id=id)
            data1=Education(reg_id=candidate_instance,course=course,university=university,year=year)
            data1.save()
        success = True   
    # return render(request,'edit.html',{'success': success})
    
    return HttpResponse("ok", status=200)


