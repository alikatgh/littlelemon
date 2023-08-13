from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import BookingSerializer
from .models import Booking
from rest_framework import generics
from .serializers import MenuSerializer
from .models import Menu
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

from django.http import HttpResponse


# def sayHello(request):
#     return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = [IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})
