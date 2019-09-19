from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.template.defaultfilters import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class TournamentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, unique=True)
    player1 = models.CharField(max_length=30)
    player2 = models.CharField(max_length=30)
    player3 = models.CharField(max_length=30)
    player4 = models.CharField(max_length=30)
    player5 = models.CharField(max_length=30)
    player6 = models.CharField(max_length=30)
    player7 = models.CharField(max_length=30)
    player8 = models.CharField(max_length=30)
    stared_at = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TournamentModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'TournamentModel'

    def __str__(self):
        return self.name


class MatchModel(models.Model):
    tournament_matches = models.ForeignKey(TournamentModel, on_delete=models.CASCADE)
    player1 = models.CharField(max_length=30)
    player2 = models.CharField(max_length=30)
    score1 = models.ImageField(default=0)
    score2 = models.ImageField(default=0)


class All_tournaments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    player1 = models.CharField(max_length=30)
    player2 = models.CharField(max_length=30)
    player3 = models.CharField(max_length=30)
    player4 = models.CharField(max_length=30)
    player5 = models.CharField(max_length=30)
    player6 = models.CharField(max_length=30)
    player7 = models.CharField(max_length=30)
    player8 = models.CharField(max_length=30)
    date_posted = models.DateTimeField(default=timezone.now)
    stared_at = models.DateField(default=timezone.now)
    # slug = models.SlugField(unique=True, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})