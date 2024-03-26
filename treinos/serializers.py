from rest_framework.serializers import ModelSerializer
from treinos.models import Exercicio


class ExercicioSerializer(ModelSerializer):
    class Meta:
        model = Exercicio
        fields = '__all__'