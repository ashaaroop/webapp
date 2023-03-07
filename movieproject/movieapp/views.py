from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import MovieForm

# Create your views here.

def index(request):
    item=movie.objects.all()
    context={
        'movie_list':item
    }
    return render(request,'index.html',context)
def details(request,movie_id):
    token=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'token':token})


def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        des = request.POST.get('des')
        year = request.POST.get('year')
        img = request.FILES['img']
        item=movie(name=name,des=des,year=year,img=img)
        item.save()
    return render(request,"add.html")

def update(request,id):
    item1=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=item1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form1':form,'item1':item1})

def delete(request,id):
    if request.method=='POST':
        item=movie.objects.get(id=id)
        item.delete()
        return redirect('/')
    return render(request,"delete.html")


