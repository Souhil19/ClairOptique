from django.contrib import admin

from django.contrib import admin
from .models import Categorie, Produit

@admin.register(Categorie, Produit)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]



"""
@admin.register(Produit)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Produit._meta.concrete_fields]
    list_filter = ('categorie', 'date_ajouté')
    search_fields = ('nom', 'brand')
    ordering = ('-date_ajouté',)
    readonly_fields = ['date_ajouté']
    fieldsets = (
        (None, {
            'fields': ('nom', 'description', 'prix', 'categorie','image','image2','image3','image4','')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('date_ajouté',),
        }),
    )"""