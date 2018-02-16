from django.db import models

# Create your models here.
class Job(models.Model):
    # null-- can be empty ; blank=False -- Required
    jobTitle        = models.CharField(max_length=120)
    company         = models.CharField(max_length=120, null=True, blank=True)
    category        = models.CharField(max_length=120, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True) # first created
    updated         = models.DateTimeField(auto_now=True)     # last updated
    # my_date_field   = models.DateField(auto_now=False, auto_now_add=False)
