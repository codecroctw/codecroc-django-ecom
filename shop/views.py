from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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


def product_detail_view(req, id):
    obj = get_object_or_404(Product, id=id)
    context = {'object': obj}
    template = 'shop/product-detail.html'

    return render(req, template, context)


def product_list_view(req):
    data = req.GET
    per_page = 6  # 每頁顯示多少個
    products = Product.objects.order_by('-updated_at')
    paginator = Paginator(products, per_page)
    page = int(data.get('p')) if data.get('p') else None
    if page:
        products = paginator.page(page)
    else:
        products = paginator.page(1)
    print(products)
    context = {'products': products.object_list}
    template = 'shop/product-list.html'

    return render(req, template, context)
