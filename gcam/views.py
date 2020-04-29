from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import GcamSerializer
from .models import Gcam


@api_view(['GET'])
def Gcamlist(request):
    gcam = Gcam.objects.all()
    serializer = GcamSerializer(gcam, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def BrandFind(request, brand):
    gcam = Gcam.objects.filter(brand=brand).all()
    serializer = GcamSerializer(gcam, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GcamDetail(request, pk):
    gcam = Gcam.objects.get(id=pk)
    serializer = GcamSerializer(gcam, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def GcamCreate(request):
    serializer = GcamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def GcamUpdate(request, pk):
    gcam = Gcam.objects.get(id=pk)
    serializer = GcamSerializer(instance=gcam, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE', 'GET'])
def GcamDelete(request, pk):
    gcam = Gcam.objects.get(id=pk)
    gcam.delete()
    return Response("done!")
