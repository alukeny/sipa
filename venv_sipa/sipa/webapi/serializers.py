from rest_framework import  serializers
from .models import orgao, categoria, posto

class orgaoSerializer(serializers.ModelSerializer):

    class Meta:
        model=orgao
        fields= ('cod_orgao','descricao','sigla','site')


class categoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model=categoria
        fields=('cod_categoria', 'descricao')

class postoSerializer(serializers.ModelSerializer):
    orgao = serializers.StringRelatedField(many=False)
    categoria = serializers.StringRelatedField(many=False)

    class Meta:
        model = posto
        fields = ('cod_posto','descricao','nif','tel','email','endereco', 'orgao', 'categoria')