from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)  # Título del post
    slug = models.SlugField(max_length=200, unique=True)  # Slug para URLs amigables
    content = models.TextField()  # Contenido del post
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Imagen opcional
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Relación con el autor
    categories = models.ManyToManyField('Category', related_name='posts', blank=True)  # Categorías opcionales
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)  # Etiquetas opcionales
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización
    is_published = models.BooleanField(default=False)  # Publicado o borrador

    class Meta:
        ordering = ['-created_at']  # Ordenar por fecha de creación, más reciente primero
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})  # URL amigable para el detalle del post


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre único de la categoría
    slug = models.SlugField(max_length=100, unique=True, db_index=True)  # Slug para URLs amigables

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})  # URL amigable para la categoría


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Nombre único de la etiqueta
    slug = models.SlugField(max_length=50, unique=True, db_index=True)  # Slug para URLs amigables

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})  # URL amigable para la etiqueta


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Relación con el post
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Usuario que comenta
    content = models.TextField()  # Contenido del comentario
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    is_approved = models.BooleanField(default=False)  # Moderación

    class Meta:
        ordering = ['-created_at']  # Ordenar comentarios por fecha de creación
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f'Comentario de {self.user.username} en "{self.post.title}" ({self.created_at})'
