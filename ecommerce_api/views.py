from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Category, Product, Order,Cart
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer, CartSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViewSet(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


    def list(self,request):
        filtered_queryset = self.filter_queryset(queryset=self.queryset)
        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self,request, pk=None):
        instance = self.queryset.get(pk=pk)
        if instance:
            serializer = self.serializer_class(instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self,request,pk=None):
        instance = self.queryset.get(pk=pk)
        if instance:
            serializer = self.serializer_class(instance=instance,data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        return Response(status=status.HTTP_404_NOT_FOUND)
    

    def partial_update(self,request,pk=None):
        instance = self.queryset.get(pk=pk)
        if instance:
            serializer = self.serializer_class(instance=instance,data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        return Response(status=status.HTTP_404_NOT_FOUND)
    

    def destroy(self,request, pk=None):
        instance = self.queryset.get(pk=pk)
        if instance:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
        



class OrderViewSet(GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def list(self,request):
        filtered_queryset = self.filter_queryset(queryset=self.queryset)
        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

    def retrieve(self,request, pk=None):
        instance = self.queryset.get(pk=pk)
        if instance:
            serializer = self.serializer_class(instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_404_NOT_FOUND) 

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request, pk=None):
        instance = self.queryset.get(pk=pk)
        if instance:
            serializer = self.serializer_class(instance=instance,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def partial_update(self, request,pk=None):
        instance = self.queryset.get(pk=pk)
        if instance:
            serializer = self.serializer_class(instance=instance,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    def destroy(self,request,pk=None):
        instance = self.queryset.get(pk=pk)
        if instance:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    

