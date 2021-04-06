from django.contrib import admin
from django.urls import path, include
from .views import index, post_details, sobre, contato, salvar_comentario, index_admin2, add_post, edit_post, excluir_post

# http://127.0.0.1:/blog
# http://127.0.0.1:/blog/postagens
# http://127.0.0.1:/blog/
urlpatterns = [
    path('', index, name='index'),
    path('post/<int:id>', post_details, name='post_details'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('salvar-comentario/<int:id>', salvar_comentario, name="salvar_comentario"),
    path('admin2/', index_admin2, name='index_admin2'),
    path('admin2/add-post', add_post, name='add_post'),
    path('admin2/edit-post/<int:id_post>', edit_post, name='edit_post'),
    path('admin2/excluir-post/<int:id_post>', excluir_post, name='excluir_post'),

]
