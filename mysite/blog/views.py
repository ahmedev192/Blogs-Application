from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("No Post found.")
#     return render(
#         request,
#         'blog/post/detail.html',
#         {'post': post}
#     )

def post_detail(request,year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )