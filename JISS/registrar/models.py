
from django.db import models

class courtcases(models.Model):   
    cin = models.IntegerField(unique=True,blank=True,null=True)
    defendant = models.CharField(max_length=200)
    defendant_address = models.CharField(max_length=1000)
    crimetype = models.CharField(max_length=100)
    date= models.DateField(blank=True,null=True)
    location = models.CharField(max_length=1000,blank=True)
    arresting_officer = models.CharField(max_length=200)
    when_arrested = models.DateField()
    status = models.BooleanField(default=True)
    presiding_judge = models.CharField(max_length=200)
    public_prosecuter = models.CharField(max_length=200)
    lawyer = models.CharField(max_length=200)
    starting_date = models.DateField()
    expected_completion_date = models.DateField()
    #
    hearing_date = models.DateField(blank=True,null=True)
    #
    judgement_date = models.DateField(blank=True,null=True)
    attending_judge = models.CharField(max_length=200,blank=True)
    judgement_summary = models.TextField(max_length=10000,blank=True)
    

class hearing_details(models.Model):
    cin = models.IntegerField(verbose_name="CIN",primary_key=True)
    date = models.DateField()
    hearing_summary = models.TextField(max_length=10000)

class period(models.Model):
    starting_date = models.DateField()
    end_date = models.DateField()

class hearing_date(models.Model):
    cin = models.IntegerField()
    date = models.DateField()

class search_by_cin(models.Model):
    cin = models.IntegerField()

class judgement(models.Model):
    cin = models.IntegerField()
    judgement_date = models.DateField(blank=True,null=True)
    attending_judge = models.CharField(max_length=200,blank=True)
    judgement_summary = models.TextField(max_length=10000,blank=True)