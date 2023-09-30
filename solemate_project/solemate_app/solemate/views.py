from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("solemate/index.html")
    return HttpResponse(template.render(request=request))

def results(request):
    template = loader.get_template("solemate/results.html")
    return HttpResponse(template.render(request=request))