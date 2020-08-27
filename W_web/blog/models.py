from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)

    slug = models.SlugField(unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category/{}/'.format(self.slug)

    class Meta:
        verbose_name_plural='categories'

class Post(models.Model):
    title = models.CharField(max_length=15, null=False, verbose_name="게시물 이름")
    content = MarkdownxField(verbose_name="게시물 내용")

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="작성 시간")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, blank=True,null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return '{} :: {}'.format(self.title,self.author)

    def get_update_url(self):
        return self.get_absolute_url() + 'update/'

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)

    def get_markdown_content(self):
        return markdown(self.content)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modfied_at = models.DateTimeField(auto_now=True)
    def get_markdown_content(self):
        return markdown(self.text)

    def get_absolute_url(self):
        return self.post.get_absolute_url() + '#comment-id-{}'.format(self.pk)