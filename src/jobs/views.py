import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
# Function based views
def home(request):
    num = None
    some_list = [
        random.randint(0, 10000),
        random.randint(0, 10000),
        random.randint(0, 10000)
    ]
    conditional_bool_item = False
    if conditional_bool_item:
        num = random.randint(0, 10000)
    context = {
        "num": num,
        "some_list": some_list
    }
    return render(request, "home.html", context)

def about(request):
    context = {
    }
    return render(request, "about.html", context)

def contact(request):
    context = {
    }
    return render(request, "contact.html", context)

class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)
class ContactView(TemplateView):
    template_name = 'contact.html'
