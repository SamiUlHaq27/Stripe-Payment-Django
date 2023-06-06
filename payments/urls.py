from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('success/', views.success),
    path('cancel/', views.cancel),
    path('checkout/<int:pid>', views.checkout, name="checkout")
]
