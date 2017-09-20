# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import News

from django.shortcuts import render

def homepage(request):
    return render(request, 'core/home_page.html')

def news(request):
    news = News.objects.all()
    return render(request, 'core/news.html', {'news': news})

def news_detail(request, news_id=1):
    new = News.objects.get(id = news_id)
    return render(request, 'core/new.html', {'new': new})

def test(request):
    return render(request, 'core/test.html')


