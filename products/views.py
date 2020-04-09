from rest_framework import generics, mixins
from .models import Products
from .serializer import ProductSerializer


# Create your views here.

class ProductApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "slug"
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.all()

class ProductApiCreateList(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = "slug"
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.all()

    def post(self,request, *args, **kwargs):
        return self.create(request,*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user =self.request.user)