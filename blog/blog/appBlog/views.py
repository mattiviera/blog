from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
#creo las vistas
def post_list(request):
    posts = Post.objects.filter(is_published=True)  # Filtrar solo los posts publicados
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(is_published=True)  # Obtener los posts de esa categoría
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts.filter(is_published=True)  # Obtener los posts con esa etiqueta
    return render(request, 'blog/tag_detail.html', {'tag': tag, 'posts': posts})
