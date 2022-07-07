from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic import View
from registrar.models import courtcases
from django.views.generic.list import ListView
from django.utils import timezone
from .forms import resolved_case_details

def lawyer(request):
    template = loader.get_template('lawyer.html')
    return HttpResponse(template.render())

class pastcase(View):
    form_class = resolved_case_details
    template_name = 'lawyer/resolved_case_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        template = 'searched_case.html'
        if form.is_valid():
            temp = form.cleaned_data['cin']
            cases = courtcases.objects.filter(cin = temp)

            context = {
                'object_list':cases
            }
            return render(request,template,context)

        return render(request, self.template_name, {'form': form})


            

        
