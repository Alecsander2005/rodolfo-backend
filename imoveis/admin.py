from django.contrib import admin
from .models import Imovel, Imagem

class ImagemInline(admin.TabularInline):
    model = Imagem
    extra = 1

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]
    list_display = ('id', 'titulo', 'preco', 'cidade', 'tipo')