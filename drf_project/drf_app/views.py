from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
# Create your views here.

class ColorCreateListUpdateRetrieveDelete(APIView):
    def post(self,request):
        color_serializer=ColorSerializers(data=request.data)
        if color_serializer.is_valid():
            color_serializer.save()
            return Response(color_serializer.data,status=status.HTTP_201_CREATED)
        return Response(color_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,id=None):
        if id is None:
            colors=Color.objects.all()
            colors_serializers=ColorSerializers(colors,many=True)
            return Response(colors_serializers.data,status=status.HTTP_204_NO_CONTENT)
        else:
            try:
                color=Color.objects.get(id=id)
            except Color.DoesNotExist:
                return Response({"message":f"Color with id {id} does not exist"},status=status.HTTP_404_NOT_FOUND)
            
            color_serializers=ColorSerializers(color)
            return Response(color_serializers.data,status=status.HTTP_200_OK)
    
    def patch(self,request,id):
        try:
            color=Color.objects.get(id=id)
        except Color.DoesNotExist:
            return Response({"message":f"Color with id {id} does not exist"},status=status.HTTP_404_NOT_FOUND)

        color_serializer=ColorSerializers(color,data=request.data,partial=True)
        if color_serializer.is_valid():
            color_serializer.save()
            return Response(color_serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(color_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            color=Color.objects.get(id=id)
        except Color.DoesNotExist:
            return Response({"message":f"Color with id {id} does not exist"},status=status.HTTP_404_NOT_FOUND)
        color.delete()
        return Response({"message":f"Color with id {id} deleted successfully"},status=status.HTTP_202_ACCEPTED)        


class ProductCreateListUpdateRetrieveDelete(APIView):
    def get(self,request,id=None):
        if id is None:
            products=Product.objects.all()
            product_serializers=ProductSerializers(products,many=True)
            return Response(product_serializers.data,status=status.HTTP_200_OK)
        else:
            try:
                product=Product.objects.get(id=id)
            except:
                return Response({"message":f"Product with id {id} does not exist!"},status=status.HTTP_404_NOT_FOUND)
            product_serializer=ProductSerializers(product)
            return Response(product_serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        product_serializer=ProductSerializers(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data,status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            product=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({"message":f"Product with id {id} does not exist"},status=status.HTTP_404_NOT_FOUND)

        product_serializer=ProductSerializers(product,data=request.data,partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            product=Product.objects.get(id=id)
        except:
            return Response({"message":f"Product with id {id} does not exist!"},status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message":f"Product with id {id} deleted successfully"},status=status.HTTP_200_OK)