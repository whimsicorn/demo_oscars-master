from django.forms import ModelForm
from .models import Films

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'polish_title', 'director', 'year', 'country', 'description', 'poster']
