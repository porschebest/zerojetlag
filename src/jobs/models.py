from django.db import models

# Create your models here.
class JobInfo(models.Model):
    # null-- can be empty ; blank=False -- Required
    JobTitle        = models.CharField(max_length=120)
    Company         = models.CharField(max_length=120, null=True, blank=True)
    Logo            = models.CharField(max_length=120, null=True, blank=True)
    Category        = models.CharField(max_length=120, null=True, blank=True)
    DeadLine        = models.CharField(max_length=120, null=True, blank=True)
    VideoLink       = models.CharField(max_length=120, null=True, blank=True)
    JobDescription  = models.CharField(max_length=500, null=True, blank=True)
    JobRequirements = models.CharField(max_length=500, null=True, blank=True)
    Career          = models.CharField(max_length=500, null=True, blank=True)
    InterviewExp    = models.CharField(max_length=500, null=True, blank=True)
    Timestamp       = models.DateTimeField(auto_now_add=True) # first created
    Updated         = models.DateTimeField(auto_now=True)     # last updated

    # my_date_field   = models.DateField(auto_now=False, auto_now_add=False)
    # def __str__(self):
    #     return self.jobTitle
