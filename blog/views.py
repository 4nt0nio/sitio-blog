from django.shortcuts import render

def lista_posts(request):
	return render(request, 'blog/lista_posts.html', {})
