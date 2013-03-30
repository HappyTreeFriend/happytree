#!/usr/bin/env python
#coding=utf-8

from django.http import Http404,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Article,Tag,Comment

# Create your views here.

def home(request):
	'''首页'''
	try:
		articles = Article.objects.values('id','title','content','tag')
		navs = {'url':'add','name':u'写日志'}
		#print articles
		#import pdb
		#pdb.set_trace()
		return render_to_response('home.html',{'articles':articles,'navs':navs},context_instance=RequestContext(request));
	except ValueError:
		raise Http404

def add_article(request):
	'''增加文章'''
	try:
		tags = Tag.objects.values('id','t_name')
		print tags
		return render_to_response('edit_article.html',{'tags':tags,'post_action':'/blog/add/post_article/'},context_instance=RequestContext(request))
	except ValueError:
		raise Http404

def show_article(request,a_id):
	'''查看文章'''
	try:
		article = Article.objects.get(id=a_id)
		comment = Comment.objects.get(article_id=a_id)
		return render_to_response('show_article.html',{'article':article,'comment':comment},context_instance=RequestContext(request))
	except ValueError:
		raise Http404

def post_article(request):
	try:
		#my_obj = {'title':request.POST['title'],'content':request.POST['content'],'author':request.user,'tag':request.POST['tags']}
		my_obj = {'title':request.POST['title'],'content':request.POST['content'],'author':'natsuki','tag':request.POST['tags']}
		Article().post_article(**my_obj)
		return HttpResponse('post success!')
	except ValueError:
		raise Http404
