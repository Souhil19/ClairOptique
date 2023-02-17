from django.shortcuts import render
from rest_framework import generics

from django.http import Http404
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Produit, Categorie
from .serializers import ProductSerializer, CategorySerializer, CategoryItemSerializer

"""
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 9"""

class ProductsList(generics.ListCreateAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProductSerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Produit.objects.all()[0:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Produit.objects.filter(categorie__ref=category_slug).get(ref=product_slug)
        except Produit.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategoryItemSerializer


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Categorie.objects.get(slug=category_slug)
        except Categorie.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class ProductListByCategory(generics.ListAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProductSerializer
#    pagination_class = PageNumberPagination
#    pagination_class.page_size = 9

    def get_queryset(self):
        category = self.kwargs['category_slug']
        return self.queryset.filter(categorie__ref=category)

class Search(generics.ListCreateAPIView):
    search_fields = ['nom','brand']
    filter_backends = (filters.SearchFilter,)
    queryset = Produit.objects.all()
    serializer_class = ProductSerializer
#    pagination_class = StandardResultsSetPagination