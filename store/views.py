from django.http import HttpResponse
from django.shortcuts import redirect, render , get_object_or_404
from django.urls import reverse 
from django.utils import timezone
from store.models import Produits , Panier, Order
from django.contrib import messages
# Create your views here.


def index(request):
    produit= Produits.objects.all()

    context={
        'produit': produit 
    }
    return render(request , 'store/index.html', context)


def detail_produit(request, slug):
    produit = get_object_or_404(Produits,slug=slug)
    context = {
        'produit': produit
    }
    return render(request, 'store/detail.html', context)


def ajouter_produit(request,slug):
    user = request.user
    produit = get_object_or_404(Produits,slug=slug)
    panier,_ =Panier.objects.get_or_create(user=user)
    order,created_order=Order.objects.get_or_create(user=user,commandé=False,produit=produit)

    if created_order:
        panier.orders.add(order)
        panier.save()
    else:
        order.quantite +=1
        order.save()
    
    return redirect(reverse('produit',kwargs={'slug': slug}))


def panier(request):
    panier = get_object_or_404(Panier , user=request.user)
    total_achat = panier.calcul_achat_total()
    context ={
        "orders":panier.orders.all(),
        "total_achat":total_achat
    }
    return render(request, 'store/panier.html', context)


def supprimer_panier(request):
    if panier :=  request.user.panier:
        panier.delete()
    return redirect('index')


def valider_achat(request):
   panier = get_object_or_404(Panier , user=request.user)

   for order in panier.orders.all():
       order.commandé = True
       order.date_commande = timezone.now()
       order.save()

   panier.orders.clear()
   panier.save()

   messages.success(request, 'Votre achat a été validé avec succès. Merci!')
   return redirect('index')