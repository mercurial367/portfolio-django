from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):

    blog_posts = Blog.objects.all()
    return render(request, 'Blogs/blog.html', {'blog_posts':blog_posts})

def post(request, post_id):

    post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'Blogs/post.html', {'post':post})
