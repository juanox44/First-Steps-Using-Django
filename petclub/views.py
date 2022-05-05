from django.shortcuts import render

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView


class PersonAPIView(APIView):
    def get(self, request):
        return Response(data="estoy en el get del PersonApiView", status=200)

    def patch(self, request):
        return Response(data="Estoy en el patch del PersonApiView", status=200) # respuesta del servicio

    def delete(self, request):
        return Response(data="Estoy en el delete del PersonApiView", status=200) # respuesta del servicio

    def post(self, request):
        return Response(data="Estoy en el post del PersonApiView", status=200) # respuesta del servicio


class PetAPIView(APIView):
    def get(self, request):
        return Response(data="estoy en el get del PetApiView", status=200)

    def patch(self, request):
        return Response(data="Estoy en el patch del PetApiView", status=200) # respuesta del servicio

    def delete(self, request):
        return Response(data="Estoy en el delete del PetApiView", status=200) # respuesta del servicio

    def post(self, request):
        return Response(data="Estoy en el post del PetApiView", status=200) 
