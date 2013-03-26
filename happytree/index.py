#!/usr/bin/env python
#coding=utf-8

from django.http import HttpResponse,HttpResponseRedirect

def hello(request):
	return HttpResponseRedirect('/blog')
	
def test(request):
	return HttpResponse('Hello django!')
