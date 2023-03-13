from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *

#importer le formulaire
from .forms import *

def index(request):
    form = FormTask(request.POST or None)
    list = Task.objects.all()
    
    context = {
        'form': form,
        'taches' : list,
    }

    if form.is_valid():
        form.save()
        return redirect('/')
        
    return render(request, 'index.html', context)


def update(request, my_id):
    obj =  get_object_or_404(Task, id = my_id)
    #instance est ce qui sera recharger dans le form
    form = FormTask(request.POST or None, instance=obj) 
    if form.is_valid():
        form.save()
        return redirect('/') #page mere
    
    return render(request, 'update.html', {'form':form})

def delete(request, my_id):
    obj = get_object_or_404(Task, id= my_id)
    
    obj.delete()
    return redirect('/') #page mere
        

