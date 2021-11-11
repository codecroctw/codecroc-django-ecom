from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from shop.models import Product

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
        data = req.POST
        mytext = data.get('mytext')
        print(mytext)
        print(req.META)
    return render(req, template_name='shop/test-form.html')


def product_detail_view(req):
    if req.method == 'GET':
        data = req.GET
        product_id = data.get('p')
    #obj = get_object_or_404(Product, id=product_id)
        # try:
        #    obj = Product.objects.get(id=product_id)
        # except:
        #    raise Http404

        qs = Product.objects.filter(id=product_id)
        if not qs.exists() and qs.count() != 1:
            raise Http404
        else:
            obj = qs.first()
    context = {'object': obj}
    template = 'shop/product-detail.html'

    return render(req, template, context)
