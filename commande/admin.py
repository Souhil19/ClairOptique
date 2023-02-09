from django.contrib import admin

from .models import Commande,ArticleCommande

@admin.register(ArticleCommande)
class UniversalAdmin(admin.ModelAdmin):
    search_fields = ['Address ', 'nom' , 'prenom']
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Commande._meta.concrete_fields]
    search_fields = ['address ', 'nom', 'prenom']
    list_filter = ( 'crée_le',)
    ordering = ('-crée_le',)
    readonly_fields = ['crée_le']
    fieldsets = (
        (None, {
            'fields': ('nom','prenom','address','wilaya','phone','prix_total')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('crée_le',),
        }),
    )