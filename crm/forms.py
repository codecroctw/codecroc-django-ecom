from django import forms


class TestForm(forms.Form):
	q = forms.CharField(label="搜尋")