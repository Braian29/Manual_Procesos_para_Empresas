#post\views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from post.models import Post, Interes
from post.forms import FormularioBuscarPosts
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)
'''
    VISTAS BASADAS EN FUNCIONES:
    -    Ver posts: Muestro TODOS las paginas creadas por los usuarios
    - Buscar posts: Filtro paginas por titulo
'''


@login_required
def ver_posts(request):
    posts = Post.objects.all()

    # Agrega la lógica para comprobar si a cada post le interesa al usuario
    posts_con_interes = []
    for post in posts:
        le_interesa = Interes.objects.filter(usuario=request.user, publicacion=post).exists()
        posts_con_interes.append((post, le_interesa))
    print(posts)
    return render(request, 'post/ver_posts.html', {'posts_con_interes': posts_con_interes})


def buscar_posts(request):
    titulo = request.GET.get('titulo', None)

    if titulo:
        posts = Post.objects.filter(titulo__icontains=titulo)
    else:
        posts = Post.objects.all()

    posts = posts.order_by('id')

    formulario_buscar_posts = FormularioBuscarPosts()

    return render(request, 'post/buscar_posts.html', { 'formulario_buscar_posts' : formulario_buscar_posts, 'posts' : posts })

'''
    CLASES BASADAS EN VISTAS (CBV):
    -    Ver: VerPostView
    -  Crear: NuevoPostView
    - Editar: EditarPostView
    - Borrar: EliminarPostView
'''
class VerPostView(DetailView):
    model         = Post
    template_name = 'post/ver_post.html'


class NuevoPostView(LoginRequiredMixin, CreateView):
    model         = Post
    template_name = 'post/crear_post.html'
    success_url   = '/posts/'
    fields        = ['titulo', 'subtitulo', 'contenido', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EditarPostView(LoginRequiredMixin, UpdateView):
    model         = Post
    template_name = 'post/editar_post.html'
    success_url   = '/posts/'
    fields        = ['titulo', 'subtitulo', 'contenido', 'imagen']


class EliminarPostView(LoginRequiredMixin, DeleteView):
    model         = Post
    template_name = 'post/borrar_post.html'
    success_url   = '/posts/'

@login_required
def detalle_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    usuario = request.user
    le_interesa = Interes.objects.filter(usuario=usuario, publicacion=post).exists()

    if request.method == 'POST':
        if le_interesa:
            Interes.objects.filter(usuario=usuario, publicacion=post).delete()
        else:
            Interes.objects.create(usuario=usuario, publicacion=post)
        return HttpResponseRedirect(reverse('ver_post', args=[post_id]))

    return render(request, 'post/ver_post.html', {'post': post, 'le_interesa': le_interesa})
