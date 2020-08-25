from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created') #작성일의 역순으로 게시물 출력력

#def index(request):
#     posts = Post.objects.all()
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts
#         }
#     )