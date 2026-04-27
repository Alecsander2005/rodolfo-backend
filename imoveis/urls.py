from django.urls import path
from .views import (
    ImovelListView,
    ImovelDetailView,
    ImovelCreateView,
    ImovelUpdateView,
    ImovelDeleteView,
    delete_imagem,
    api_imoveis_list,
    api_imovel_detail,
)

urlpatterns = [
    path('api/imoveis/', api_imoveis_list, name='api_imoveis_list'),
    path('api/imoveis/<int:pk>/', api_imovel_detail, name='api_imovel_detail'),
    path('', ImovelListView.as_view(), name='imovel_list'),
    path('<int:pk>/', ImovelDetailView.as_view(), name='imovel_detail'),
    path('novo/', ImovelCreateView.as_view(), name='imovel_create'),
    path('editar/<int:pk>/', ImovelUpdateView.as_view(), name='imovel_update'),
    path('deletar/<int:pk>/', ImovelDeleteView.as_view(), name='imovel_delete'),
    path('imagem/<int:pk>/deletar/', delete_imagem, name='imagem_delete'),
]