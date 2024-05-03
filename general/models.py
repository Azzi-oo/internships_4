from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    friends = models.ManyToManyField(
        to="self",
        symmetrical=True,
        blank=True,
    )


class Post(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=64)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    is_published = models.BooleanField(default=False)


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
