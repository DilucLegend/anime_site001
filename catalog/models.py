from django.db import models

# Create your models here.
class Category(models.Model):
    objects = models.Model

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Anime(models.Model):
    objects = models.Model

    anime_image = models.ImageField(null=True, blank=True, upload_to='media')
    name = models.CharField(max_length=100)
    number_of_episodes = models.IntegerField()
    year_first_episode = models.CharField(max_length=5)
    year_last_episode = models.CharField(max_length=5)
    anime_rating = models.CharField(max_length=5)
    anime_genres = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    anime_url = models.CharField(max_length=100)

    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name