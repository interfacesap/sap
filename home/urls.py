from django.urls import path
from .views import *

urlpatterns = [
  path("nivelAcesso/", nivelAcessoView.as_view(), name='nivelAcesso'),
  path('nivelAcesso/<int:pk>/', nivelAcessoView.as_view(), name='nivelAcessoParameters'),

  path("centroCusto/", centroCustoView.as_view(), name='centroCusto'),
  path('centroCusto/<int:pk>/', centroCustoView.as_view(), name='centroCustoParameters'),

  path("tipoMovimento/", tipoMovimentoView.as_view(), name='tipoMovimento'),
  path('tipoMovimento/<int:pk>/', tipoMovimentoView.as_view(), name='tipoMovimentoParameters'),

  path("contaRazao/", contaRazaoView.as_view(), name='contaRazao'),
  path('contaRazao/<int:pk>/', contaRazaoView.as_view(), name='contaRazaoParameters'),

  path("tipoOrdem/", tipoOrdemView.as_view(), name='tipoOrdem'),
  path('tipoOrdem/<int:pk>/', tipoOrdemView.as_view(), name='tipoOrdemParameters'),

  path("prioridade/", prioridadeView.as_view(), name='prioridade'),
  path('prioridade/<int:pk>/', prioridadeView.as_view(), name='prioridadeParameters'),

  path("localInstal/", localInstalView.as_view(), name='localInstal'),
  path('localInstal/<int:pk>/', localInstalView.as_view(), name='localInstalParameters'),

  path("tipoAtv/", tipoAtvView.as_view(), name='tipoAtv'),
  path('tipoAtv/<int:pk>/', tipoAtvView.as_view(), name='tipoAtvParameters'),

  path("CentralTrab/", CentralTrabView.as_view(), name='CentralTrab'),
  path('CentralTrab/<int:pk>/', CentralTrabView.as_view(), name='CentralTrabParameters'),

  path("Responsavel/", ResponsavelView.as_view(), name='Responsavel'),
  path('Responsavel/<int:pk>/', ResponsavelView.as_view(), name='ResponsavelParameters'),

  path("Produto/", ProdutoView.as_view(), name='Produto'),
  path('Produto/<int:pk>/', ProdutoView.as_view(), name='ProdutoParameters'),

  path("Divisao/", DivisaoView.as_view(), name='Divisao'),
  path('Divisao/<int:pk>/', DivisaoView.as_view(), name='DivisaoParameters'),

  path("TransacaoSucata/", TransacaoSucataView.as_view(), name='TransacaoSucata'),
  path('TransacaoSucata/<int:pk>/', TransacaoSucataView.as_view(), name='TransacaoSucataParameters'),

  path("TransacaoProduto/", TransacaoProdutoView.as_view(), name='TransacaoProduto'),
  path('TransacaoProduto/<int:pk>/', TransacaoProdutoView.as_view(), name='TransacaoProdutoParameters'),

  path("foto/", FotosAPIView.as_view(), name='foto'),
  path('foto/<int:pk>/', FotosAPIView.as_view(), name='fotoParameters'),

  path("Usuario/", UsuarioAPIView.as_view(), name='Usuario'),
  path('Usuario/<int:pk>/', UsuarioAPIView.as_view(), name='UsuarioParameters'),

  path("HistoricoSucata/", HistoricoSucataAPIView.as_view(), name='HistoricoSucata'),
  path('HistoricoSucata/<int:pk>/', HistoricoSucataAPIView.as_view(), name='HistoricoSucataParameters'),

  path("HistoricoProduto/", HistoricoProdutoAPIView.as_view(), name='HistoricoProduto'),
  path('HistoricoProduto/<int:pk>/', HistoricoProdutoAPIView.as_view(), name='HistoricoProdutoParameters'),

  path("Pesquisa/", PesquisaView.as_view(), name='Pesquisa'),
]