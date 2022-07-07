from django.shortcuts import render
from re import template
from django.http import HttpResponse
from django.template import loader

def judge(request):
    template = loader.get_template('judge.html')
    return HttpResponse(template.render())
