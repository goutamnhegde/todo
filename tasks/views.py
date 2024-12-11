from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .form import *



def home(request):
    tas=Tasks.objects.all()
    forms=Taskform()

    if request.method=='POST':
        forms=Taskform(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/')
    context={'tas':tas,'form':forms}
    tem=loader.get_template('home.html')
    # return render(request,'home.html',context)
    return HttpResponse(tem.render(context,request))
    


# def read(request):
#     templ=loader.get_template('list.html')
#     tas=Tasks.objects.all().values()
#     context={'tas':tas,}
#     return HttpResponse(templ.render(context,request))
# Create your views here.
