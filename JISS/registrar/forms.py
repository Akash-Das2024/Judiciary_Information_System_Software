from .models import period,courtcases,hearing_date,search_by_cin,hearing_details,judgement
from django.contrib.auth.models import User
from django import forms


class search_resolved_cases(forms.ModelForm):

    class Meta:
        model = period

        fields = ['starting_date','end_date']

class create_case(forms.ModelForm):

    class Meta:
        model = courtcases

        fields= [
            'defendant','defendant_address','crimetype','date','location','arresting_officer',
            'when_arrested','presiding_judge','public_prosecuter','lawyer','starting_date',
            'expected_completion_date'
        ]

class allot_hearing_date(forms.ModelForm):

    class Meta:
        model = hearing_date
        fields= [
            'cin','date'
            ]

class status_of_a_case(forms.ModelForm):

    class Meta:
        model = search_by_cin
        fields=[
            'cin'
            ]
class hearing_data(forms.ModelForm):

    class Meta:
        model = hearing_details

        fields = [
            'cin','date','hearing_summary'
        ]

class resolved_data(forms.ModelForm):

    class Meta:
        model = judgement

        fields = [
            'cin','judgement_date','attending_judge','judgement_summary'
        ]