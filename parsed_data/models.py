from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, upload_to="image/%Y/%m/%d")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)


    def total_likes(self):
        return self.likes.count() #likes 컬럼의 값의 갯수를 센다

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('parsed_data.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
