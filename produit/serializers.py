from rest_framework import serializers

from .models import Categorie, Produit

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = (
            "id",
            "nom",
            "brand",
            "get_absolute_url",
            "description",
            "prix",
            "promotion",
            "livraison_gratuit",
            "etoiles",
            "get_image",
            "get_image2",
            "get_image3",
            "get_image4",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Categorie
        fields = (
            "id",
            "nom",
            "get_absolute_url",
            "produits",
        )


class CategoryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = (
            "id",
            "nom",
            "get_absolute_url",
        )