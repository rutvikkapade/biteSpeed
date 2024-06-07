from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Contact
from .serializer import ContactSerializer
from .swagger_schemas import create_contact_schema

class ContactViewSet(viewsets.ViewSet):
    @create_contact_schema
    def create(self, request):
        pass