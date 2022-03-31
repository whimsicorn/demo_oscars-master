from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from app_oscars.models import Films, Review
from django.contrib.auth import get_user_model
from .forms import FilmsForm, UserReviewForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from app_oscars.tables import ReviewTable, ReviewFilter





def ranking(request):
    films = Films.objects.all()
    User = get_user_model()
    users = User.objects.all()
    reviews = Review.objects.all()
    return render(request, 'ranking.html',{'films':films,
                                           'users':users,
                                           'reviews':reviews,
                                           'filter': filter})

def films (request):
    films = Films.objects.all()
    User = get_user_model()
    users = User.objects.all()
    reviews = Review.objects.all()
    return render(request, 'films.html',{'films':films,
                                           'users':users,
                                           'reviews':reviews })



@login_required
def new_film(request):
    form = FilmsForm (request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(ranking)

    return render(request, 'film_form.html', {'form':form})

@login_required
def edit_film(request, id):
    film = get_object_or_404(Films, pk=id)
    form = FilmsForm (request.POST or None, request.FILES or None,
                      instance=film)

    if form.is_valid():
        form.save()
        return redirect(ranking)

    return render(request, 'film_form.html', {'form':form})

@login_required
def delete_film(request, id):
    films = get_object_or_404(Films, pk=id)

    if request.method == "POST":
        films.delete()
        return redirect(ranking)

    return render(request, 'confirm.html', {'films':films})


def films_rating(request, id):
    films = get_object_or_404(Films, pk=id)
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'films_rating.html', {'films':films,
                                                 'users':users})


class ReviewListView(SingleTableMixin, FilterView):

    table_class = ReviewTable
    model = Review
    template_name = 'ranking.html'
    filterset_class = ReviewFilter


def submit_review(request, film_id):

    films = Films.objects.all()
    User = get_user_model()
    users = User.objects.all()
    reviews = Review.objects.all()
    form = UserReviewForm(films)
    if request.method == "POST":
        try:
            reviews = Review.objects.get(user_id=request.user.id,films_id= film_id)
            form = UserReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request,"Dzięki za ocenę, Buło!")
            return redirect(films)
        except Review.DoesNotExist:
            if form.is_valid():
                data = Review()
                data.rating = form.cleaned_data("rating")
                data.review = form.cleaned_data("review")
                data.film_id = films.id
                data.user_id = request.user.id
                data.save()
                messages.success(request,"Dzięki za ocenę, Buło!")
                return redirect(films)

    return render(request,'films.html', {'films':films, 'users':users, 'review':reviews} )






