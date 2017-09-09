# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import News

from django.shortcuts import render

def homepage(request):
    news = News.objects.all()
    return render(request, 'core/News.html', {'news':news})
