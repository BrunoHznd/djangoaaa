from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 

    path('cadastrar-produto', views.cadastrar_produto, name='cadastrar_produto'), 

    path('listar-produto/', views.listar_produto, name='listar_produto'),
    path('excluir-produto/<int:id_produto>/', views.excluir_produto, name='excluir_produto'),
    path('editar-produto/<int:id_produto>/', views.editar_produto, name='editar_produto'),

    # rota para API
	path('produtos', views.getProdutos, name="getProdutos"),
    path('produtos/<int:id_produto>',views.getProdutoID, name="getProdutoID"),
    
    # CONSUMIR API
    path('api', views.getAPI, name='getAPI'),

    # GRAFICO 1) 29//11/2024
    path('grafico', views.grafico, name="grafico")
]
