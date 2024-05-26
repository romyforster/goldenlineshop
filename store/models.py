from django.db import models
from django.urls import reverse
from shop.settings import AUTH_USER_MODEL
from django.utils import timezone

# Create your models here.
 

class Produits(models.Model):
    nom = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    prix = models.FloatField(default=0.0)
    en_stock = models.IntegerField(default=0)
    description =  models.TextField(blank=True)
    categorie = models.TextField(blank=False)
    pic = models.ImageField(upload_to="produits", blank=True, null=True)

    def __str__(self):
        return self.nom
    
    def get_absolute_url(self):
        return reverse("produit", kwargs={"slug":self.slug})
    
#table commander article
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL , on_delete=models.CASCADE)
    produit = models.ForeignKey(Produits,on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    commandé = models.BooleanField(default=False)
    date_commande = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.produit.nom} ({self.quantite})"    


#table panier

class Panier(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
  


    def __str__(self):
        return self.user.username
    
    def delete(self, *args,**kwargs):
        for order in self.orders.all():
            order.commandé = True
            order.date_commande = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args,**kwargs)
    
    def calcul_achat_total(self):
        total_achat = 0
        for order in self.orders.all():
            total_achat += order.produit.prix * order.quantite
        return total_achat
    

    

     