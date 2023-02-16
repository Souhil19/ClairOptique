from rest_framework import serializers

from .models import Commande, ArticleCommande

from produit.serializers import ProductSerializer


class ArticleCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCommande
        fields = (
            "nom_produit",
            "prix",
            "produit",
            "quantite",
        )


class CommandeSerializer(serializers.ModelSerializer):
    articles = ArticleCommandeSerializer(many=True)

    class Meta:
        model = Commande
        fields = (
            "id",
            "prenom",
            "nom",
            "address",
            "wilaya",
            "phone",
            "livraison_gratuit",
            "articles",
            "prix_total"
        )

    def create(self, validated_data):
        articles_data = validated_data.pop('articles')
        commande = Commande.objects.create(**validated_data)

        for article_data in articles_data:
            ArticleCommande.objects.create(commande=commande, **article_data)

        return commande