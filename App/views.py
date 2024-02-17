from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
def products_dummy(request):
    # Dummy products list
    dummy_products = [
        {
            'title': 'Product 1',
            'description': 'Description for Product 1',
            'price': 10.99,
            'created_at': '2024-02-17T12:00:00Z'
        },
        {
            'title': 'Product 2',
            'description': 'Description for Product 2',
            'price': 19.99,
            'created_at': '2024-02-17T13:00:00Z'
        },
    ]
    return JsonResponse(dummy_products, safe=False)