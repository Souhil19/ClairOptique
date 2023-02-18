from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    ref = models.SlugField()

    class Meta:
        ordering = ('nom',)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return f'/{self.ref}/'


class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, related_name='products', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default='')
    ref = models.SlugField()
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=6, decimal_places=0)
    promotion = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    etoiles = models.IntegerField(max_length=1, default=5)
    livraison_gratuit = models.BooleanField( default=False)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads/', blank=True, null=True)

    date_ajouté = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_ajouté',)

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return f'/{self.categorie.ref}/{self.ref}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_image2(self):
        if self.image2:
            return 'http://127.0.0.1:8000' + self.image2.url
        return ''

    def get_image3(self):
        if self.image3:
            return 'http://127.0.0.1:8000' + self.image3.url
        return ''

    def get_image4(self):
        if self.image4:
            return 'http://127.0.0.1:8000' + self.image4.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
