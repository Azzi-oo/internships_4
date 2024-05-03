from django.db import models


class CustomUserManager(models.Manager):
    def users_with_many_friends(self):
        return self.annotate(num_friends=models.Count('friends')).filter(num_friends__gt=100)


class CustomPostManager(models.Manager):
    def latest_published_posts(self):
        return self.filter(is_published=True).order_by('-created_at')[:25]


class CustomCommentManager(models.Manager):
    def comments_by_specific_user(self, username):
        return self.filter(author__username=username)
