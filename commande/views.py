from django.shortcuts import render

from django.shortcuts import render

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Commande, ArticleCommande
from .serializers import CommandeSerializer



class Commande(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

    def perform_create(self, serializer):
        paid_amount = sum(
            item.get('quantite') * item.get('produit').prix * (1 - item.get('produit').promotion)  for item in serializer.validated_data['articles'])
        tarif_livraison = serializer.validated_data['tarif_livraison']
        paid_amount = paid_amount + tarif_livraison
        serializer.save( prix_total=paid_amount)