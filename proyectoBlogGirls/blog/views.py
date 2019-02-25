from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    # post = Post.objects.filter(published_date__lte = timezone.now())
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post' : post})