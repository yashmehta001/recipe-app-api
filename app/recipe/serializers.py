from rest_framework import serializers

from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    "serializer tag object"

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    "Serializer for ingredient object"

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)
