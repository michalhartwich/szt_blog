from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post


def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/index.html', context)

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/show.html', {'post': post})
