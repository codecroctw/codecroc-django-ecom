from django.shortcuts import render

from .forms import TestForm

def search_view(req):
    form = TestForm()
    if req.method == 'GET':
        print(req.GET)
    if req.method == 'POST':
        print(req.POST)
    return render(req, 'search-form.html', {'form': form})