from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipe

from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    "Base viewset for user owned recipe attr"
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        "return objects for current authenticated user"
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        "create new ingredient"
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    "manage tags the database"
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
    "manage ingredients in database"
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    "manage recipes in database"
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        "retrieve recipes for authenticated user"
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        "return serializer class"
        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        "create new recipe"
        serializer.save(user=self.request.user)
