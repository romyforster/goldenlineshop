PRESENTATION DU PROJET GOLDENLINE

golden line est application de vente de vetement qui permet au clients de constituer leur panier et payer a la caisse de la boutique .
le clients a un compte utilisateur qui lui permet de beneficier des certains avantages lorsqu'il effectue un achat dans l'une des boutique Goldenline
## TECHONOLOGIE DE DEVELOPPEMENT 

**DATABASE:** mysql

**BACKEND:** PYTHON DJANGO
**FRONTEND** HTML

## Usage/Examples

```python

""presentation des models""

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
```

User stoty

1-inscription et creation de compte utilisateur.
2-le client ajoute des produit au panier(selction des produits dans le magasin par le clients).
3- dans le model panier ,le panier calcul le total des achats effectués et renvoie au client lors de son passage a la caisse.
