from django import forms


class TestForm(forms.Form):
	some_text = forms.CharField(widget=forms.Textarea(attrs={
		'rows': 4,
		'cols': 10
	}))
	boolean = forms.BooleanField(required=False)

	INT_CHOICES = (tuple([x, x] for x in range(1, 11)))

	integer = forms.IntegerField(widget=forms.Select(choices=INT_CHOICES), initial=1)
	email = forms.EmailField(required=False)

	SOME_CHOICES = (
		('2022', '2022 紀念版'),
		('2021', '2021 經典版'),
	)

	choices = forms.CharField(label='選項', widget=forms.Select(choices=SOME_CHOICES))

	date = forms.DateField(widget=forms.SelectDateWidget)

	def __init__(self, user=None,*args, **kwargs):
		super(TestForm, self).__init__(*args, **kwargs)
		self.fields['email'].initial = user.email


	#def clean_integer(self, *args, **kwargs):
	#	'''
	#	clean_[field_name]
	#	integer 必須 >= 10
  	#	'''
	#	integer = self.cleaned_data.get('integer')
	#	if integer < 10:
	#		raise forms.ValidationError('integer 必須 >= 10')
	#	return integer

	#def clean_some_text(self, *args, **kwargs):
	#	some_text = self.cleaned_data.get('some_text')
	#	if len(some_text) < 10:
	#		raise forms.ValidationError('Some Text 的長度需 >= 10')
	#	return some_text