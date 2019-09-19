from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# class All_tournaments(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     player1 = models.CharField(max_length=30)
#     player2 = models.CharField(max_length=30)
#     player3 = models.CharField(max_length=30)
#     player4 = models.CharField(max_length=30)
#     player5 = models.CharField(max_length=30)
#     player6 = models.CharField(max_length=30)
#     player7 = models.CharField(max_length=30)
#     player8 = models.CharField(max_length=30)
#     date_posted = models.DateTimeField(default=timezone.now)
#     stared_at = models.DateField(default=timezone.now)
#     slug = models.SlugField(unique=True, )
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={'pk': self.pk})