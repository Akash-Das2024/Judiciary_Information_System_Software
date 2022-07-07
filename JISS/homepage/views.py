#views
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic import View
from django.views.generic.list import ListView
from django.utils import timezone
from .forms import get_user
from .models import MyUsers

def home(request): 
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def help(request):
    template = loader.get_template('help.html')
    return HttpResponse(template.render())

class login(View):
    form_class = get_user
    template_name = 'homepage/signin_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            users = MyUsers.objects.filter(email = email,username = username)
            for user in users:
                if user.is_registrar == True:
                    template = template = loader.get_template('registrar.html')
                    return HttpResponse(template.render())
                if user.is_lawyer == True:
                    template = template = loader.get_template('lawyer.html')
                    return HttpResponse(template.render())
                if user.is_judge == True:
                    template = template = loader.get_template('judge.html')
                    return HttpResponse(template.render())

        return render(request, self.template_name, {'form': form})

