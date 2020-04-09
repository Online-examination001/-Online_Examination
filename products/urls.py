from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('products/', views.ProductApiCreateList.as_view(), name='products'),

    path('products/<slug>/', views.ProductApiView.as_view())
]

