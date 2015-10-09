from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def lista_posts(request):
	posts = Post.objects.filter(published_date__lte=timezone.now())
	return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalle_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/detalle_post.html', {'post': post})

def nuevo_post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.detalle_post', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/editar_post.html', {'form': form})

def editar_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.detalle_post', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/editar_post.html', {'form': form})