from django.db import models


class Post(models.Model):
    creator = models.TextField()
    text = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
