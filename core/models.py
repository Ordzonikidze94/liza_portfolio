# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class News(models.Model):
    class Meta():
        db_table = "news"

    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title