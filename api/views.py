from django.shortcuts import render,  get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse_lazy


from .serializers import ProductSerializer, DataSerializer
from .models import Product
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.


"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }

    return Response(api_urls);

"""

@api_view(['GET'])
def ShowAll(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def DeleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response("Item Deleted Successfully..!")

#@api_view(['GET'])
#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
    model = Product
    #form_class = DataSerializer
    template_name = 'home.html'


class AddProductView(CreateView):
    model = Product
    form_class = DataSerializer
    template_name = 'create_product.html'
    success_url = reverse_lazy('home')
   

class UpdateProductView(UpdateView):
    model = Product
    form_class = DataSerializer
    template_name = 'update_product.html'
    success_url = reverse_lazy('home')

class DeleteProductView(DeleteView):
    model = Product
    template_name ='delete_product.html'
    success_url = reverse_lazy('home')

