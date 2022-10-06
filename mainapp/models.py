from django.db import models
# from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model

User = get_user_model()


# class User(AbstractUser):

# @property
# def count_likes(self):
#     return self.likes.count()


class Post(models.Model):
    name = models.CharField(max_length=127)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.name

    @property
    def likes_amount(self):
        return self.likes.all().count()

    def unlikes_amount(self):
        return self.unlikes.all().count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.name


class Unlike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='unlikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='unlikes')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.name
