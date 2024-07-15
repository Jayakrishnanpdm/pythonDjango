from django.shortcuts import render
from .models import movie_info
from . forms import MovieForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login/')
def create(request):
    
    if request.POST:
      frm=MovieForm(request.POST,request.FILES)
      if frm.is_valid():
          frm.save()
    else:
        frm=MovieForm()      
        return render(request,'create.html',{'frm':frm})

@login_required(login_url='login/')
def list(request):
    movie_set=movie_info.objects.all()
    return render(request,'list.html',{'movies':movie_set})

def edit(request,pk):
    instance_to_edited=movie_info.objects.get(pk=pk)
    if request.POST:
        frm=MovieForm(request.POST,instance=instance_to_edited)
        if frm.is_valid():
         frm.save()
    else:
       frm=MovieForm(instance=instance_to_edited) 
            
    return render(request,'create.html',{'frm':frm})


def delete(request,pk):
    instance=movie_info.objects.get(pk=pk)
    instance.delete()
    movie_set=movie_info.objects.all()
    return render(request,'list.html',{'movies':movie_set})