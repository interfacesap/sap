from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.pagination import PageNumberPagination
from django.db import connection
import cx_Oracle as Database
from django.shortcuts import render
import cx_Oracle

def getPagination(request, listItems):

    if 'page' in request.GET:
        try:
            parameter_page = request.GET['page']
            if (int(parameter_page) <= 0):
                parameter_page = '1'
            page = Paginator(listItems, 10)
            return [page.page(parameter_page), page.count, page.num_pages]
        except (EmptyPage, PageNotAnInteger):
            return [page.page(1), 0, 0]
    else:
        return [listItems, 0, 0]
# ----------------------------------------------------------------------------------------------
class PesquisaView(APIView):
    """
    API pesquisa
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
            if 'produto' in request.GET:            
                produto = request.GET['produto']
                redlakeSearch(produto)
                return Response({"msg": "Pesquisa realizada com sucesso!!"})
#-----------------------------------------------------------------------------------------#
def redlakeSearch(produto):
    connection = cx_Oracle.connect(user="lge1ca", password="Safira2021!leo",dsn="redlake_dwhp.world")
    cursor = connection.cursor()
    sql = """SELECT MARD.MATNR, MARD.LABST, MAKT.MAKTX
    FROM INFM_PSLA_CSC2.V_REPL_MARD_B2 MARD
    inner join INFM_PSLA_CSC2.V_REPL_MAKT_B2 MAKT
    ON MARD.MATNR = MAKT.MATNR
    where MARD.MATNR = :mid
    and MARD.WERKS = '908A'
    and MARD.LABST <> 0"""
    cursor.execute(sql, mid=produto)

    for row in cursor:
        print(row)
# -------------------------------------------------------------------------------------------
class nivelAcessoView(APIView):
    """
    API nivelAcesso
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        # redlakeSearch()
        if 'nivel' in request.GET:            
            nivel = request.GET['nivel']
            Acesso = nivelAcesso.objects.filter(id=nivel)
            serializer = nivelAcessoSerializer(Acesso, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            Acesso = nivelAcesso.objects.get(id=pk)
            serializer = nivelAcessoSerializer(Acesso)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            Acesso = nivelAcesso.objects.all()
            serializer = nivelAcessoSerializer(Acesso, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = nivelAcessoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        Acesso = nivelAcesso.objects.get(id=pk)
        serializer = nivelAcessoSerializer(Acesso, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        Acesso = nivelAcesso.objects.get(id=pk)
        Acesso.delete()
        return Response({"msg": "Apagado com sucesso"})
#-----------------------------------------------------------------------------------------#
class centroCustoView(APIView):
    """
    API centroCusto
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'centro' in request.GET:            
            centro = request.GET['centro']
            custo = centroCusto.objects.filter(id=centro)
            serializer = centroCustoSerializer(custo, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            custo = centroCusto.objects.get(id=pk)
            serializer = centroCustoSerializer(custo)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            custo = centroCusto.objects.all()
            serializer = centroCustoSerializer(custo, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = centroCustoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        custo = centroCusto.objects.get(id=pk)
        serializer = centroCustoSerializer(custo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        Acesso = centroCusto.objects.get(id=pk)
        Acesso.delete()
        return Response({"msg": "Apagado com sucesso"}) 
#----------------------------------------------------------------------#
class tipoMovimentoView(APIView):
    """
    API tipoMovimento
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'tipo' in request.GET:            
            tipo = request.GET['tipo']
            movimento = tipoMovimento.objects.filter(id=tipo)
            serializer = tipoMovimentoSerializer(movimento, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            movimento = tipoMovimento.objects.get(id=pk)
            serializer = tipoMovimentoSerializer(movimento)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            movimento = tipoMovimento.objects.all()
            serializer = tipoMovimentoSerializer(movimento, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = tipoMovimentoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        movimento = tipoMovimento.objects.get(id=pk)
        serializer = tipoMovimentoSerializer(movimento, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        movimento = tipoMovimento.objects.get(id=pk)
        movimento.delete()
        return Response({"msg": "Apagado com sucesso"}) 
#-----------------------------------------------------------------------------------------#
class contaRazaoView(APIView):
    """
    API contaRazao
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'conta' in request.GET:            
            conta = request.GET['conta']
            razao = contaRazao.objects.filter(id=conta)
            serializer = contaRazaoSerializer(razao, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            razao = contaRazao.objects.get(id=pk)
            serializer = contaRazaoSerializer(razao)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            razao = contaRazao.objects.all()
            serializer = contaRazaoSerializer(razao, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = contaRazaoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        razao = contaRazao.objects.get(id=pk)
        serializer = contaRazaoSerializer(razao, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        razao = contaRazao.objects.get(id=pk)
        razao.delete()
        return Response({"msg": "Apagado com sucesso"}) 
#---------------------------------------------------------------------
class tipoOrdemView(APIView):
    """
    API tipoOrdem
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'ordem' in request.GET:            
            ordem = request.GET['ordem']
            dados = tipoOrdem.objects.filter(id=ordem)
            serializer = tipoOrdemSerializer(dados, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            dados = tipoOrdem.objects.get(id=pk)
            serializer = tipoOrdemSerializer(dados)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            dados = tipoOrdem.objects.all()
            serializer = tipoOrdemSerializer(dados, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = tipoOrdemSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        dados = tipoOrdem.objects.get(id=pk)
        serializer = tipoOrdemSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = tipoOrdem.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"}) 
#---------------------------------------------------------------------#
class prioridadeView(APIView):
    """
    API prioridade
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'priori' in request.GET:
            priori = request.GET['priori']
            info = prioridade.objects.filter(id=priori)
            serializer = prioridadeSerializer(info, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            info = prioridade.objects.get(id=pk)
            serializer = prioridadeSerializer(info)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            info = prioridade.objects.all()
            serializer = prioridadeSerializer(info, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = prioridadeSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        info = prioridade.objects.get(id=pk)
        serializer = prioridadeSerializer(info, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        info = prioridade.objects.get(id=pk)
        info.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class localInstalView(APIView):
    """
    API localInstal
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'local' in request.GET:
            local = request.GET['local']
            infos = localInstal.objects.filter(id=local)
            serializer = localInstalSerializer(infos, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            infos = localInstal.objects.get(id=pk)
            serializer = localInstalSerializer(infos)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            infos = localInstal.objects.all()
            serializer = localInstalSerializer(infos, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = localInstalSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        infos = localInstal.objects.get(id=pk)
        serializer = localInstalSerializer(infos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        infos = localInstal.objects.get(id=pk)
        infos.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class tipoAtvView(APIView):
    """
    API tipoAtv
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'atividade' in request.GET:
            atividade = request.GET['atividade']
            inf = tipoAtv.objects.filter(id=atividade)
            serializer = tipoAtvSerializer(inf, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            inf = tipoAtv.objects.get(id=pk)
            serializer = tipoAtvSerializer(inf)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            inf = tipoAtv.objects.all()
            serializer = tipoAtvSerializer(inf, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = tipoAtvSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        inf = tipoAtv.objects.get(id=pk)
        serializer = tipoAtvSerializer(inf, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        inf = tipoAtv.objects.get(id=pk)
        inf.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class CentralTrabView(APIView):
    """
    API CentralTrab
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'central' in request.GET:
            central = request.GET['central']
            inform = CentralTrab.objects.filter(id=central)
            serializer = CentralTrabSerializer(inform, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            inform = CentralTrab.objects.get(id=pk)
            serializer = CentralTrabSerializer(inform)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            inform = CentralTrab.objects.all()
            serializer = CentralTrabSerializer(inform, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = CentralTrabSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        inform = CentralTrab.objects.get(id=pk)
        serializer = CentralTrabSerializer(inform, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        inform = CentralTrab.objects.get(id=pk)
        inform.delete()
        return Response({"msg": "Apagado com sucesso"})
 #---------------------------------------------------------------------#
class ResponsavelView(APIView):
    """
    API Responsavel
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'respon' in request.GET:
            respon = request.GET['respon']
            dado = Responsavel.objects.filter(id=respon)
            serializer = ResponsavelSerializer(dado, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            dado = Responsavel.objects.get(id=pk)
            serializer = ResponsavelSerializer(dado)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            dado = Responsavel.objects.all()
            serializer = ResponsavelSerializer(dado, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = ResponsavelSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        dado = Responsavel.objects.get(id=pk)
        serializer = ResponsavelSerializer(dado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dado = Responsavel.objects.get(id=pk)
        dado.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class ProdutoView(APIView):
    """
    API Produto
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'prod' in request.GET:
            prod = request.GET['prod']
            dad = Produto.objects.filter(id=prod)
            serializer = ProdutoSerializer(dad, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            dad = Produto.objects.get(id=pk)
            serializer = ProdutoSerializer(dad)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            dad = Produto.objects.all()
            serializer = ProdutoSerializer(dad, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        dad = Produto.objects.get(id=pk)
        serializer = ProdutoSerializer(dad, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dad = Produto.objects.get(id=pk)
        dad.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class DivisaoView(APIView):
    """
    API Divisao
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'div' in request.GET:
            div = request.GET['div']
            dadoss = divisao.objects.filter(id=div)
            serializer = divisaoSerializer(dadoss, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            dadoss = divisao.objects.get(id=pk)
            serializer = divisaoSerializer(dadoss)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            dadoss = divisao.objects.all()
            serializer = divisaoSerializer(dadoss, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = divisaoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        dadoss = divisao.objects.get(id=pk)
        serializer = divisaoSerializer(dadoss, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dadoss = divisao.objects.get(id=pk)
        dadoss.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class TransacaoSucataView(APIView):
    """
    API TransacaoSucata
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'Sucata' in request.GET:
            Sucata = request.GET['Sucata']
            infoss = TransacaoSucata.objects.filter(id=Sucata)
            serializer = TransacaoSucataSerializerRead(infoss, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            infoss = TransacaoSucata.objects.get(id=pk)
            serializer = TransacaoSucataSerializerRead(infoss)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            infoss = TransacaoSucata.objects.all()
            serializer = TransacaoSucataSerializerRead(infoss, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = TransacaoSucataSerializerRead(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        infoss = TransacaoSucata.objects.get(id=pk)
        serializer = TransacaoSucataSerializerRead(infoss, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        infoss = TransacaoSucata.objects.get(id=pk)
        infoss.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class TransacaoProdutoView(APIView):
    """
    API TransacaoProduto
    """

    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'prod' in request.GET:
            prod = request.GET['prod']
            base = TransacaoProduto.objects.filter(id=prod)
            serializer = TransacaoProdutoSerializer(base, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            base = TransacaoProduto.objects.get(id=pk)
            serializer = TransacaoProdutoSerializer(base)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            base = TransacaoProduto.objects.all()
            serializer = TransacaoProdutoSerializer(base, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = TransacaoProdutoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        base = TransacaoProduto.objects.get(id=pk)
        serializer = TransacaoProdutoSerializer(base, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        base = TransacaoProduto.objects.get(id=pk)
        base.delete()
        return Response({"msg": "Apagado com sucesso"})
# ---------------------------------------------------------------------#
class FotosAPIView(APIView):
    """
    API Fotos
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'produto' in request.GET:   
            produto = request.GET['produto']
            fotos = Fotos.objects.filter(idProdutoFK=produto)
            resp = getPagination(request, fotos)
            serializer = FotosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        elif pk != '':
            fotos = Fotos.objects.get(id=pk)
            serializer = FotosSerializer(fotos)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        else:
            fotos = Fotos.objects.all()
            resp = getPagination(request, fotos)
            serializer = FotosSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )


    def post(self, request):
        serializer = FotosSerializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        # return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        fotos = Fotos.objects.get(id=pk)
        serializer = FotosSerializer(fotos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        fotos = Fotos.objects.get(id=pk)
        fotos.delete()
        return Response({"msg": "Apagado com sucesso"})

class UsuarioAPIView(APIView):
    """
    API Usuario
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'user' in request.GET:
            user = request.GET['user']
            usuarios = Usuario.objects.filter(user=user)
            serializer = UsuarioSerializer(usuarios, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )            
        elif pk == '':
            usuarios = Usuario.objects.all()
            resp = getPagination(request, usuarios)
            serializer = UsuarioSerializer(resp[0], many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': resp[1],
                    'pages': resp[2]
                }
            )
        else:
            usuarios = Usuario.objects.get(idUserFK=pk)
            serializer = UsuarioSerializer(usuarios)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )


    def post(self, request):        
        serializer = UsuarioSerializer(data=request.data, many=True)      
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        usuarios = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        usuarios = Usuario.objects.get(id=pk)
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})
#-------------------------------------------------------------------------
class HistoricoSucataAPIView(APIView):
    """
    API HistoricoSucata
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'sucata' in request.GET:            
            sucata = request.GET['sucata']
            hist = HistoricoSucata.objects.filter(id=sucata)
            serializer = HistoricoSucataSerializer(hist, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            hist = HistoricoSucata.objects.get(id=pk)
            serializer = HistoricoSucataSerializer(hist)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            hist = HistoricoSucata.objects.all()
            serializer = HistoricoSucataSerializer(hist, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = HistoricoSucataSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        hist = HistoricoSucata.objects.get(id=pk)
        serializer = HistoricoSucataSerializer(hist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        hist = HistoricoSucata.objects.get(id=pk)
        hist.delete()
        return Response({"msg": "Apagado com sucesso"})
#-----------------------------------------------------------------------------------------#
class HistoricoProdutoAPIView(APIView):
    """
    API HistoricoProduto
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
        if 'sucata' in request.GET:            
            sucata = request.GET['sucata']
            histo = HistoricoProduto.objects.filter(id=histo)
            serializer = HistoricoProdutoSerializer(histo, many=True)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )
        elif pk != '':
            histo = HistoricoProduto.objects.get(id=pk)
            serializer = HistoricoProdutoSerializer(histo)
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )      
        else:            
            histo = HistoricoProduto.objects.all()
            serializer = HistoricoProdutoSerializer(histo, many=True)            
            return Response(
                {
                    'data': serializer.data,
                    'total': 0,
                    'pages': 0
                }
            )

    def post(self, request):
        serializer = HistoricoProdutoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
  
    def put(self, request, pk=''):
        histo = HistoricoProduto.objects.get(id=pk)
        serializer = HistoricoProdutoSerializer(histo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        histo = HistoricoProduto.objects.get(id=pk)
        histo.delete()
        return Response({"msg": "Apagado com sucesso"})
# -------------------------------------------------------------------------------------

    

