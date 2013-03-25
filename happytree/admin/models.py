#!/usr/bin/env python
#coding:utf-8

import re
from django import forms
from django.db.models import F
from django.db import models
from django.contrib import admin
from happytree.blog.models import Tag,Article,Comment

# Create your models here.

class ArticleAdmin(admin.ModelAdmin):
	raw_id_fields = ('author','tag')

class TagAdmin(admin.ModelAdmin):
	raw_id_fields = ('author',)

class CommentAdmin(admin.ModelAdmin):
	raw_id_fields = ('author',)

admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
