from django.test import TestCase
from django.test import TestCase
from .models import Produits
from .models import Panier, Produits
from .models import order, Panier

# Create your tests here.

class ProduitsModelTest(TestCase):

    def test_create_products(self):
        """Teste la création d'un produit."""
        produit = Produit.objects.create(nom="chemise", prix=50.00, description="Une belle chemise")
        self.assertEqual(produits.nom, "chemise")
        self.assertEqual(produits.prix, 20.00)
        self.assertEqual(produits.description, "chemise")

    def test_update_products(self):
        """Teste la mise à jour d'un produit."""
        produits = Produits.objects.create(nom="chemise", prix=50.00, description="une belle chemise")
        produits.nom = "Chemise"
        produits.prix = 30.00
        produits.save()
        self.assertEqual(produits.nom, "Chemise")
        self.assertEqual(produits.prix, 30.00)

    def test_delete_products(self):
        """Teste la suppression d'un produit."""
        produits = Produits.objects.create(nom="chemise", prix=50.00, description="une belle chemise")
        produits.delete()
        self.assertFalse(Produit.objects.exists())


class PanierModelTest(TestCase):

    def test_create_cart(self):
        """Teste la création d'un panier."""
        panier = Panier.objects.create()
        self.assertEqual(panier.lignes.count(), 0)

    def test_add_product_to_cart(self):
        """Teste l'ajout d'un produit à un panier."""
        produit = Produit.objects.create(nom="chemise", prix=50.00, description="Une belle chemise")
        panier = Panier.objects.create()
        panier.ajouter_produit(produit)
        self.assertEqual(panier.lignes.count(), 1)
        self.assertEqual(panier.total(), 20.00)

    def test_update_product_quantity_in_cart(self):
        """Teste la mise à jour de la quantité d'un produit dans un panier."""
        produit = Produit.objects.create(nom="chemise", prix=50.00, description="Une belle chemise")
        panier = Panier.objects.create()
        panier.ajouter_produit(produit)
        panier.modifier_quantite_produit(produit, 2)
        self.assertEqual(panier.lignes.count(), 1)
        self.assertEqual(panier.total(), 40.00)

    def test_remove_product_from_cart(self):
        """Teste la suppression d'un produit d'un panier."""
        produit = Produit.objects.create(nom="chemise", prix=50.00, description="Une belle chemise")
        panier = Panier.objects.create()
        panier.ajouter_produit(produit)
        panier.supprimer_produit(produit)
        self.assertEqual(panier.lignes.count(), 0)
        self.assertEqual(panier.total(), 0.00)


class orderModelTest(TestCase):

    def test_create_order(self):
        """Teste la création d'une commande."""
        panier = Panier.objects.create()
        produit = Produit.objects.create(nom="chemise", prix=50.00, description="Une belle chemise")
        panier.ajouter_produit(produit)
        commande = Commande.objects.create(panier=panier, nom_client="romy", email="romy@gmail.com")
        self.assertEqual(commande.panier, panier)
        self.assertEqual(commande.nom_client, "romy")




# Create your tests here.
