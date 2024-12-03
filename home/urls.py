from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Root URL
    path('home/', views.redirect_to_home),  # Redirect to the root URL
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
]






