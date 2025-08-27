from django.urls import path
from .views import SignupView,LoginView,LogoutView,add_to_cart,view_cart,remove_from_cart



urlpatterns=[
    path('signup/',SignupView,name='register'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView,name='logout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

]