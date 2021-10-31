from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/auth/login')
def home(req):
    # return HttpResponse('<h1>Hello World</h1>')

    return render(req, template_name='test.html')
