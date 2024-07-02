from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView)
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def index(request):
    return render(request, 'index.html', {})
