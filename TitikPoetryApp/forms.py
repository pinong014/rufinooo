from django.forms import ModelForm
from .models import Tula


class TulaForm(ModelForm):
	class Meta:
		model = Tula
		fields = '__all__'