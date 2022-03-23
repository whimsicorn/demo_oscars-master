from django.forms import ModelForm
from .models import Films, Review

class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'polish_title', 'director', 'year', 'country', 'description', 'poster']

class UserReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['points', 'review']



