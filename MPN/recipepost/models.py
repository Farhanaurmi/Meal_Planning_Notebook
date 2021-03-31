from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class Recipepost(models.Model):
    sno=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    recipe = models.TextField()
    photos = models.ImageField(default="p1.png",upload_to="images2/%y",null=True, blank=True)
    date_created = models.DateTimeField(default=now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(title=self)
        return len(ratings)

    def avg_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(title=self)
        for rating in ratings:
            sum += rating.score
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.title

class Rating(models.Model):
    title = models.ForeignKey(Recipepost, on_delete=models.CASCADE)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )