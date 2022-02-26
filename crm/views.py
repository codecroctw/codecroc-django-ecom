from django.shortcuts import render

from .forms import TestForm

def search_view(req):
    form = TestForm(data=req.POST or None, user=req.user)
    if form.is_valid():
        print(form.cleaned_data)
    return render(req, 'search-form.html', {'form': form})