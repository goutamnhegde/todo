from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .form import *
from django.views.generic import ListView


def addtask(request):
    #  tas=Tasks.objects.all()
     

     if request.method=='POST':
          tak=request.POST.get('tk')
          d1=request.POST.get('d1')
          if d1:
            t=Tasks(Title=tak,Date=d1)
            t.save()
          else:
            t=Tasks(Title=tak,Date=date.today())
            t.save()
          return redirect('/')
     d=request.GET.get('dat')
     if d:
        tas=Tasks.objects.filter(Date=d).exclude(Completed=True)
     else:
         tas=Tasks.objects.filter(Date=date.today()).exclude(Completed=True)
        
     context={'tas':tas}
     tem=loader.get_template('home.html')
    # # return render(request,'home.html',context)
     return HttpResponse(tem.render(context,request))


def done(request,id):
    md=Tasks.objects.get(id=id)
    md.Completed=True
    md.save()
    return redirect('/')

def delet(request,id):
    did=Tasks.objects.get(id=id)
    did.delete()
    return redirect('/')
   






# class tasklist(ListView):
#     model=Tasks
#     template_name='home.html'




# def read(request):
#     templ=loader.get_template('list.html')
#     tas=Tasks.objects.all().values()
#     context={'tas':tas,}
#     return HttpResponse(templ.render(context,request))
# Create your views here.
