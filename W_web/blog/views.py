from django.shortcuts import render
from .models import Post ,Category
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created') #작성일의 역순으로 게시물 출력력

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList,self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['uncategory'] =Post.objects.filter(category=None).count()
        context['all_post'] =Post.objects.count()
        return context


class PostDetail(DetailView):
    model = Post

class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug']

        if slug == '_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created') #작성일의 역순으로 게시물 출력력

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self),self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['uncategory'] =Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']
        if slug == '_none':
            context['category'] = '미분류'
        else:
            category = Category.objects.get(slug=slug)
            context['category'] = category
        # context['title'] = 'BLOG - {}'.format(category.name)
        return context


# def post_detail(request, pk):
#     blog_post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail_html',
#         {
#             'blog_post':blog_post,
#         }
#     )

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