from django.http import HttpResponse
from rest_framework import viewsets
from cars4share.models import User
from cars4share.serializers import UserSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello! You are at Cars4Share index page!")


# API view for User
class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UserSerializer

    queryset = User.objects.all()
