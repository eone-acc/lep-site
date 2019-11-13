from django.shortcuts import render
from .admin import *

def index(request):

    # posts = Post.objects.all().order_by('pub_date')[:3]
    posts_images = PostImage.objects.filter(status=True).order_by('-post__pub_date')[:3]

    return render(request, 'landing/index.html', locals())


def vuetest(request):
    return render(request, 'landing/vuetest.html')


def about(request):
    return render(request, 'landing/about.html', locals())

def project(request):
    posts_images = PostImage.objects.filter(status=True)

    return render(request, 'landing/projects.html', locals())

def contacts(request):
    return render(request, 'landing/contacts.html', locals())

def detail(request, slug):

    context = Post.objects.get(slug=slug)

    return render(request, 'landing/detail.html', locals())

