from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog , category

# Create your views here.

def index(request): 
    context = {
        "blogs": Blog.objects.filter(is_active=True , is_home=True),
        "categories": category.objects.all()
    }
    return render(request, "blog/index.html", context) # contet yukarıda yazdım 

def blogs(request): 
    context = {
        "blogs":Blog.objects.filter(is_active=True ),
        "categories": category.objects.all()
    }
    return render(request, "blog/blogs.html",context)

def blog_details (request , slug):
    blog= Blog.objects.get(slug=slug)
    return render(request , "blog/blogs-detail.html " , {
        "blog": blog
    } )

def blogs_by_category(request , slug ):
     context = {
        "blogs" :category.objects.get(slug=slug).blog_set.filter( is_active=True ),
        "categories": category.objects.all(),
        "selected_category" : slug
    }
     return render(request, "blog/blogs.html",context)


