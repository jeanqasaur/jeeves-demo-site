from django.template import RequestContext
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
import urllib
import random

def index(request):
  return render_to_response("index.html"
           , { 'which_page': "home" })

def jconf_view(request):
  return render_to_response("jconf.html"
          , { 'which_page': "jconf" })

def jcourse_view(request):
  return render_to_response("jcourse.html"
          , { 'which_page': "jcourse" })

def hipaa_view(request):
  return render_to_response("hipaa.html"
          , { 'which_page': "hipaa" })

def about_view(request):
  return render_to_response( "about.html"
         , { 'which_page' : "about" } )
