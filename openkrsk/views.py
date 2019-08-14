from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse, Http404
from urllib.parse import urlparse


from django import forms
from django.contrib import admin

from easy_maps.widgets import AddressWithMapWidget
# Create your views here.

def Short_Articles_view(request):
    sections=Section.objects.all()

    return render(request, 'main.html', {'sections': sections})

def Articles_view(request, offset):
    try:
        offset=int(offset)
        posts = Article.objects.filter(Tag=offset).order_by('id')
        tag=Section.objects.filter(id=offset)
        return render(request, 'tag.html', {'posts': posts, 'tag': tag})
    except ValueError:
        raise HttpResponse('Does not exist')

def Article_view(request, post_id):
    try:
        post_id=int(post_id)
        req = urlparse(request.META.get('HTTP_REFERER')).path
        post=Article.objects.filter(id=post_id)
        return render(request, 'article.html', {'post': post, 'req': req})
    except ValueError:
        raise HttpResponse('Does not exist')



