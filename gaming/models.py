from django.conf import settings
from django.db import models
from django.utils import timezone

class usernames(models.Model):
    # Creating a table with 3 columns. The first column is the author, the second column is the game,
    # and the third column is the username.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def publish(self):
        # Saving the date and time of when the username was created.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # Returning the game name.
        return self.game
