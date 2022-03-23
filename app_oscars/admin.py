from django.contrib import admin
from .models import Films, Review, TableReview

@admin.register(Films)
class FilmAdmin (admin.ModelAdmin):
    list_display = ['title','director','country']
    list_filter = ['country']
    search_fields=['title','description']

admin.site.register(Review)
admin.site.register(TableReview)



