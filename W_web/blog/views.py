from django.shortcuts import render, redirect
from .models import Post ,Category , Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title', 'content', 'head_image', 'category'
    ]

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail,self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['uncategory'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm()
        return context


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = [
        'title', 'content', 'head_image', 'category'
    ]

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(type(self),self).form_valid(form)
        else:
            return redirect('/blog/')

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

def new_comment(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(comment.get_absolute_url())
    else:
        redirect('/blog/')

def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url() + '#comment-list')
    else:
        return redirect('/blog/')

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