from django.db import models
from produit.models import Produit


class Commande(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    wilaya = models.CharField(max_length=100)
    #tarif_livraison= models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    phone = models.CharField(max_length=100)
    crée_le = models.DateTimeField(auto_now_add=True)
    prix_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['-crée_le', ]

    def __str__(self):
        return self.nom +' '+ self.prenom


class ArticleCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='articles', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name='articles', on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=8, decimal_places=2)

    nom_produit=models.CharField(max_length=100, default="")
    quantite = models.IntegerField(default=1)
    #discount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return '%s' % self.id