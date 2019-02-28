from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm
from .models import Post

# Create your views here.

def post_list(request):
    # post = Post.objects.filter(published_date__lte = timezone.now())
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post' : post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html',{'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # messages.success(request, 'realizado')
            # con el http response se puede redireccioner de la misma forma.
            # return HttpResponseRedirect("/")
            return redirect('post_detail', pk = post.pk) 
    else:
        form = PostForm()
        return render(request,'blog/post_new.html',{'form' : form})

def post_edit(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request,'blog/post_new.html',{'form' : form})

def post_delete(request, pk):
    post_delete = get_object_or_404(Post, pk=pk)
    post_delete.delete()
    return redirect('/')
