#!/usr/bin/env python
#coding=utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponseRedirect('/blog')
	
def test(request):
	return HttpResponse('Hello django!')
	
def my_404_view(request):
	return render_to_response('404.html');
