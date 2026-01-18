from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
#   from .models import Product    # zahashowane w ramach task 5 lesson 25
#   from .serializers import ProductSerializer    # zahashowane w ramach task 5 lesson 25
from rest_framework.decorators import api_view    #  dodane w ramach task 5 lesson 25
from rest_framework.response import Response    #  dodane w ramach task 5 lesson 25

#  class ProductViewSet(ModelViewSet):    # zahashowane w ramach task 5 lesson 25
#       queryset = Product.objects.all()   # zahashowane w ramach task 5 lesson 25
#       serializer_class = ProductSerializer   # zahashowane w ramach task 5 lesson 25

#  dodane w ramach task 5 lesson 25
@api_view(['GET'])
def set_name(request):
    name = request.GET.get('name')
    response = Response({"message": f"Ustawiono imię: {name}"})
    if name:
        response.set_cookie('user_name', name)
    return response
    
#  dodane w ramach task 5 lesson 25
@api_view(['GET'])
def hello(request):
    name = request.COOKIES.get('user_name')

    if name:
        return Response({"message": f"Witaj, {name}!"})
    else:
        return Response({"message": "Witaj, Gość!"})

