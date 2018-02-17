from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import JobInfo

def jobs_listview(request):
    template_name = 'jobs/jobs_list.html'
    queryset = JobInfo.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class JobListView(ListView):
    # template_name = 'jobs/jobs_list.html'
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = JobInfo.objects.filter(
                Q(Category__iexact=slug) | Q(Category__icontains=slug) |
                Q(Company__iexact=slug)  | Q(Company__icontains=slug)  |
                Q(JobTitle__iexact=slug) | Q(JobTitle__icontains=slug)
            )
        else:
            queryset = JobInfo.objects.all()
        return queryset
