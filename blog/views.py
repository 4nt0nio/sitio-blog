from django.shortcuts import render
from django.utils import timezone
from .models import Post

def lista_posts(request):
	posts = Post.objects.filter(published_date__lte=timezone.now())
	return render(request, 'blog/lista_posts.html', {'posts': posts})
