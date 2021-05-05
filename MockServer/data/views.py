from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import DataSerializer
from .models import Data

# Create your views here.
class DataListCreateAPIView(ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer