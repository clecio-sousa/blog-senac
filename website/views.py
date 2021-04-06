from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comentario

from .forms import PostForm
from django.utils import timezone



# Create your views here.

def index(request):
    lista_posts = Post.objects.all()

    dados = {

        'Posts': lista_posts
    }
    return render(request, "index.html", dados)


def post_details(request, id):
    post = Post.objects.get(id=id)
    comentarios = Comentario.objects.filter(aula=id)

    dados = {
        'Postagem': post,
        'Comentario': comentarios
    }
    return render(request, 'postagem.html', dados)


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')


def salvar_comentario(request, id):
    post = Post.objects.get(id=id)

    Comentario.objects.create(
        aula=post,
        nome_aluno=request.POST['nome'],
        comentario=request.POST['comentario'],
        sexo=request.POST['sexo']
    )
    return redirect('post_details', post.id)


def index_admin2(request):
    lista_posts = Post.objects.all()
    dados = {
        'Posts': lista_posts
    }

    return render(request, 'index_admin2.html', dados)


def add_post(request):
    form_class = PostForm
    form = form_class(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form = PostForm(request.POST, request.FILES)
            f = form.save(commit=False)
            f.cadastrado = timezone.now()
            f.alterado = timezone.now()
            f.save()
            return redirect('index_admin2')

    else:
        form = PostForm

    dados = {
        'form': form
    }
    return render(request, 'add_editar_admin2.html', dados)


def edit_post(request, id_post):
    form_class = PostForm
    form = form_class(request.POST or None)
    post = get_object_or_404(Post, id=id_post) # verifica se existe esse obj no BD

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            f = form.save(commit=False)
            f.cadastrado = timezone.now()
            f.alterado = timezone.now()
            f.save()
            return redirect('index_admin2')

    else:
        form = PostForm(instance=post)

    dados = {
        'form': form
    }
    return render(request, 'add_editar_admin2.html', dados)


def excluir_post(request, id_post):
    post = Post.objects.get(id=id_post)
    if post:
        post.delete()

    return redirect('index_admin2')

