from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=15, null=False, verbose_name="게시물 이름")
    content = models.TextField(null=False ,verbose_name="게시물 내용")

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)

    created = models.DateTimeField(null=False, verbose_name="작성 시간")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} :: {}'.format(self.title,self.author)