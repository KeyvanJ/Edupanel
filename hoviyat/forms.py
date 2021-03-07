from django import forms
from .models import homework


class hwform(forms.ModelForm):
	class Meta:
		model = homework
		fields = ('title', 'description', 'pdf')