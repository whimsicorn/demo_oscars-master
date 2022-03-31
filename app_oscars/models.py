from django.db import models
from django.contrib.auth import get_user_model



class Films(models.Model):
    COUNTRIES = [
        ('US','Stany Zjednoczone'),
        ('GB',"Wielka Brytania"),
        ('JP','Japonia'),
    ]
    title = models.CharField(max_length=40,default="", blank=True)
    polish_title = models.CharField(max_length=40,default="", blank=True)
    director = models.CharField(max_length=30,default="", blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRIES, default='US')
    description = models.TextField(max_length=500,default="Film oskarowy", blank=True)
    poster = models.ImageField(upload_to='posters', null=True,blank=True)

    def __str__(self):
        return self.polish_title+" ("+self.title+") "+", "+self.director


class Review(models.Model):
    films = models.ForeignKey(Films, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    points = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return "Ocena "+self.user.username+" "+self.films.title




#to be deleted
class TableReview(models.Model):
    filmtitle = models.ForeignKey(Films,on_delete=models.CASCADE)
    user = models.ForeignKey (get_user_model(), on_delete=models.CASCADE)
    pointsforthisfilm = models.ForeignKey(Review, on_delete=models.CASCADE)




