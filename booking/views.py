from rest_framework import viewsets
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from rest_framework.filters import SearchFilter
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.js', {'form': form})

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['flight']
    permission_classes = [IsAuthenticated]
