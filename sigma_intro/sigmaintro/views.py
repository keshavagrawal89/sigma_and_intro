from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def home(request):
    variables = {
        'title': 'Welcome to weird place!',
        'heading': 'Hello Homies'
    }

    return render_to_response('index.html', RequestContext(request, variables))

