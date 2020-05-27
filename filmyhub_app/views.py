from django.shortcuts import render,HttpResponse
from filmyhub_app.models import contact,movies
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import datetime






def index(request):
    movie_list=movies.objects.all()
    paginator=Paginator(movie_list,6)
    page=request.GET.get('page')
    
    try:
        movie=paginator.page(page)
    except PageNotAnInteger:
        movie=paginator.page(1)
    except EmptyPage:
        movie=paginator.page(paginator.num_page)
        
    
    
    return render(request,'index.html',{'movies':movie})
    #return HttpResponse('this is home page')


def hollywood(request):
    movie_list=movies.objects.filter(movie_type='hollywood')
    paginator=Paginator(movie_list,6)
    page=request.GET.get('page')
    
    try:
        movie=paginator.page(page)
    except PageNotAnInteger:
        movie=paginator.page(1)
    except EmptyPage:
        movie=paginator.page(paginator.num_page)
        
    
    return render(request,'hollywood.html',{'movies':movie})




def bollywood(request):
    movie_list=movies.objects.filter(movie_type='bollywood')
    paginator=Paginator(movie_list,6)
    page=request.GET.get('page')
    
    try:
        movie=paginator.page(page)
    except PageNotAnInteger:
        movie=paginator.page(1)
    except EmptyPage:
        movie=paginator.page(paginator.num_page)
        
    
    return render(request,'bollywood.html',{'movies':movie})
    

def top_imdb(request):
    return HttpResponse('this is top-imdb page')

def contact1(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        cont=contact(email=email,password=password)
        cont.save()
        
    return render(request,'contact.html')
# Create your views here.
