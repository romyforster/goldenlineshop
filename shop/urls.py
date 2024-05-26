"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import index , detail_produit , ajouter_produit , panier,supprimer_panier,valider_achat
from comptes.views import signup ,logout_user,login_user

from django.conf.urls.static import static

from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('produits/<str:slug>', detail_produit, name='produit'),
    path("signup/",signup, name="signup"),
    path('login/',login_user,name="login"),
    path('panier/',panier,name="panier"),
    path('panier/valider_achat',valider_achat,name="valider-achat"),
    path('panier/supprimer-panier',supprimer_panier,name="supprimer-panier"),
    path("logout/",logout_user, name="logout"),
    path('produits/<str:slug>/ajouter-au-panier',ajouter_produit, name='ajouter-produit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
