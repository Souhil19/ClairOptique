from django.urls import path, include
from produit import views


urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/', views.ProductsList.as_view()),
    path('products/search/', views.Search.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('category/<slug:category_slug>/', views.ProductListByCategory.as_view()),
    path('categories/', views.CategoryListCreateAPIView.as_view()),

]