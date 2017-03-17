from django.http import HttpResponse
from rest_framework import viewsets
from cars4share import models
from cars4share import serializers


# Create your views here.
def index(request):
    return HttpResponse("Hello! You are at Cars4Share index page!")


# API view for User
class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = serializers.UserSerializer

    queryset = models.User.objects.all()

