from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(req):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(req, template_name='test.html')


@login_required(login_url='/auth/login')
def test2(req):
    return render(req, template_name='shop/test2.html')


def http_response(req):
    return HttpResponse('<h1>From Http Response</h1>')


def redirect_view(req):
    return HttpResponseRedirect('/')

def post_view(req):
    if req.method == 'POST':
        print(req.POST)
    return render(req, template_name='shop/post.html')