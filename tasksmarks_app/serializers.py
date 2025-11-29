from rest_framework import serializers
from .models import ChoiceTest


class ChoiceTestSerializer(serializers.ModelSerializer):
    """
    Серіалізатор для моделі Post
    Перетворює об'єкти Post в JSON та навпаки
    """

    class Meta:
        model = ChoiceTest
        fields = '__all__'

