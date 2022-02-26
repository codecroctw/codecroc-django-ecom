from django import forms


class TestForm(forms.Form):
	some_text = forms.CharField(required=False)
	boolean = forms.BooleanField(required=False)
	integer = forms.IntegerField()
	email = forms.EmailField(required=False)

	def __init__(self, user=None,*args, **kwargs):
		super(TestForm, self).__init__(*args, **kwargs)
		self.fields['some_text'].initial = user.userprofile_set.first().phone


	def clean_integer(self, *args, **kwargs):
		'''
		clean_[field_name]
		integer 必須 >= 10
  		'''
		integer = self.cleaned_data.get('integer')
		if integer < 10:
			raise forms.ValidationError('integer 必須 >= 10')
		return integer

	def clean_some_text(self, *args, **kwargs):
		some_text = self.cleaned_data.get('some_text')
		if len(some_text) < 10:
			raise forms.ValidationError('Some Text 的長度需 >= 10')
		return some_text