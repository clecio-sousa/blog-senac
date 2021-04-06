from django.contrib import admin
from .models import Post, Comentario #add models Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title']
    search_fields = ['title', 'sub_title']

    def get_queryset(self, request):
        return Post.objects.filter(ativado=True)

admin.site.register(Post, PostAdmin)

class ComentariAdmin(admin.ModelAdmin):
    list_display = ['nome_aluno', 'comentario', 'ativado', 'aula']
    search_fields = ['nome_aluno', 'comentario']

admin.site.register(Comentario, ComentariAdmin)
