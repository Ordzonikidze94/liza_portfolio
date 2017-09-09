# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import News

from django.shortcuts import render

def homepage(request):
    return render(request, 'core/home_page.html')

def news(request):
    news = News.objects.all()
    return render(request, 'core/news.html', {'news': news})

def test(request):
    return render(request, 'core/test.html')