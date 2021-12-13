from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http.response import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

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
    try:
        page = int(data.get('p')) if data.get('p') else None
    except:
        raise Http404
    if page:
        try:
            products = paginator.page(page)
        except:
            raise Http404
    else:
        products = paginator.page(1)

    print(paginator.count)
    print(paginator.num_pages)
    print(paginator.page_range)

    context = {
        'products': products,
        'page_range': paginator.page_range
    }
    template = 'shop/product-list.html'

    return render(req, template, context)


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product-list-generic.html'

    paginate_by = 6
    #queryset = Product.objects.filter(title='new product')

    # def get_queryset(self):
    #    return Product.objects.filter(title='new product')

    context_object_name = 'products'

    title = '商品列表'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.title
        return context


class ProductDetailMixin(object):
    title = None
    template_name = 'shop/product-detail-generic.html'

    def get_title(self):
        return self.title

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.get_title()
        return context


class ProductDetailView(LoginRequiredMixin, ProductDetailMixin, DetailView):
    login_url = '/auth/login/'

    title = 'Hello World'
    model = Product
    template_name = 'shop/product-detail-generic.html'
