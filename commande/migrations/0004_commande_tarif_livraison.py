# Generated by Django 4.1.5 on 2023-02-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0003_remove_articlecommande_quantité_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='tarif_livraison',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
