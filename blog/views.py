from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from blog.models import Blog,Contact
import math
from rest_framework.decorators import api_view
from .models import Blog
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
import requests
# Movies
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method=='GET':
        movies = Blog.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return JsonResponse({'movies':serializer.data})
    
    if request.method=='POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    




# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    no_of_posts=6
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)
   
    
    resp=requests.get('http://127.0.0.1:8000/movies/').json()
    movies=resp["movies"]
    length=len(movies)
    movies=movies[(page-1)*no_of_posts:page*no_of_posts]
    if page>1:
        prev=page-1
    else:
        prev=None
    if page<math.ceil(length/no_of_posts):
        nxt=page+1
    
    else:
        nxt=None
    context={'movies':movies,'prev':prev,'nxt':nxt}
    return render(request, 'bloghome.html',context)

def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")

        instance=Contact(name=name,email=email,phone=phone,desc=desc)
        instance.save()
    return render(request, 'contact.html')

def search(request):
    query=request.GET['query']
    blogs=Blog.objects.filter(title__icontains=query)
    if len(blogs)==0:
        blogs=Blog.objects.filter(genre__icontains=query)
    context={'blogs':blogs,'query':query }
    return render(request, 'search.html',context)


def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    


    return render(request, 'blogpost.html',context)


def mylist(request):    
    resp=requests.get('http://127.0.0.1:8000/movies/').json()
    movies=resp["movies"]
    return render(request,'hello.html',{'movies':movies})

