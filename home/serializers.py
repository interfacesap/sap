from rest_framework import serializers
from .models import *
from rest_framework import viewsets

# -------------------------------------------------------------------------
class centroCustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = centroCusto
        fields = '__all__'
class centroCustoViewSet(viewsets.ModelViewSet):
    queryset = centroCusto.objects.all()
    serializer_class = centroCustoSerializer
# -------------------------------------------------------------------------
class tipoMovimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoMovimento
        fields = '__all__'
class tipoMovimentoViewSet(viewsets.ModelViewSet):
    queryset = tipoMovimento.objects.all()
    serializer_class = tipoMovimentoSerializer
# -------------------------------------------------------------------------
class contaRazaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = contaRazao
        fields = '__all__'
class contaRazaoViewSet(viewsets.ModelViewSet):
    queryset = contaRazao.objects.all()
    serializer_class = contaRazaoSerializer
# -------------------------------------------------------------------------
class tipoOrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoOrdem
        fields = '__all__'
class tipoOrdemViewSet(viewsets.ModelViewSet):
    queryset = tipoOrdem.objects.all()
    serializer_class = tipoOrdemSerializer
# -------------------------------------------------------------------------
class prioridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = prioridade
        fields = '__all__'
class prioridadeViewSet(viewsets.ModelViewSet):
    queryset = prioridade.objects.all()
    serializer_class = prioridadeSerializer
# -------------------------------------------------------------------------
class localInstalSerializer(serializers.ModelSerializer):
    class Meta:
        model = localInstal
        fields = '__all__'
class localInstalViewSet(viewsets.ModelViewSet):
    queryset = localInstal.objects.all()
    serializer_class = localInstalSerializer
# -------------------------------------------------------------------------
class tipoAtvSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoAtv
        fields = '__all__'
class tipoAtvViewSet(viewsets.ModelViewSet):
    queryset = tipoAtv.objects.all()
    serializer_class = tipoAtvSerializer
# -------------------------------------------------------------------------
class CentralTrabSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralTrab
        fields = '__all__'
class CentralTrabViewSet(viewsets.ModelViewSet):
    queryset = CentralTrab.objects.all()
    serializer_class = CentralTrabSerializer
# -------------------------------------------------------------------------
class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'
class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
# -------------------------------------------------------------------------
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
# -------------------------------------------------------------------------
class nivelAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = nivelAcesso
        fields = '__all__'
class nivelAcessoViewSet(viewsets.ModelViewSet):
    queryset = nivelAcesso.objects.all()
    serializer_class = nivelAcessoSerializer
# -------------------------------------------------------------------------
class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = '__all__'
class FotosViewSet(viewsets.ModelViewSet):
    queryset = Fotos.objects.all()
    serializer_class = FotosSerializer
# -------------------------------------------------------------------------
class divisaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = divisao
        fields = '__all__'
class divisaoViewSet(viewsets.ModelViewSet):
    queryset = divisao.objects.all()
    serializer_class = divisaoSerializer
# -------------------------------------------------------------------------
class TransacaoSucataSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = TransacaoSucata
        fields = '__all__'
# class TransacaoSucataViewSet(viewsets.ModelViewSet):
#     queryset = TransacaoSucata.objects.all()
#     serializer_class = TransacaoSucataSerializer
# -------------------------------------------------------------------------
# class TransacaoSucataSerializerWrite(serializers.ModelSerializer):
#     class Meta:
#         model = TransacaoSucata
#         fields = ['desc','idCenTrabFK', 'txtBreve', 'trab']
# class TransacaoSucataViewSet(viewsets.ModelViewSet):
#     queryset = TransacaoSucata.objects.all()
#     serializer_class = TransacaoSucataSerializer
# -------------------------------------------------------------------------
class TransacaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransacaoProduto
        fields = '__all__'
class TransacaoProdutoViewSet(viewsets.ModelViewSet):
    queryset = TransacaoProduto.objects.all()
    serializer_class = TransacaoProdutoSerializer
# -------------------------------------------------------------------------
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
# -------------------------------------------------------------------------
class HistoricoSucataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSucata
        fields = '__all__'
class HistoricoSucataViewSet(viewsets.ModelViewSet):
    queryset = HistoricoSucata.objects.all()
    serializer_class = HistoricoSucataSerializer
# -------------------------------------------------------------------------
class HistoricoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoProduto
        fields = '__all__'
class HistoricoProdutoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoProduto.objects.all()
    serializer_class = HistoricoProdutoSerializer
# -------------------------------------------------------------------------