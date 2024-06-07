from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Contact
from .serializer import ContactSerializer
from .swagger_schemas import create_contact_schema

class ContactViewSet(viewsets.ViewSet):
    @create_contact_schema
    def create(self, request):

        """
        Create a new contact or link an existing contact based on the provided email and phone number.
        
        If neither email nor phone number exist, a new primary contact is created.
        If either email or phone number exists, a new secondary contact is created and linked to the existing primary contact.
        If both email and phone number exist in the same row, no new contact is created.
        
        Parameters:
            email (str): Email address of the contact
            phoneNumber (str): Phone number of the contact
        
        Returns:
            Response: A response containing the primary contact details and linked secondary contacts.
        """

        email = request.data.get('email')
        phoneNumber = request.data.get('phoneNumber')

        # Check if there is any contact with the same email or phoneNumber
        existing_contact_by_email = Contact.objects.filter(email=email).first()
        existing_contact_by_phone = Contact.objects.filter(phoneNumber=phoneNumber).first()
        if existing_contact_by_email and existing_contact_by_phone:
            # If both email and phone number exist in the same row, do not add any rows
            if existing_contact_by_email.id == existing_contact_by_phone.id:
                if existing_contact_by_email.linkPrecedence == 'secondary':
                    primary_contact = existing_contact_by_email.linkedId
                else:
                    primary_contact = existing_contact_by_email
                response_data = self.build_response(primary_contact)
                return Response(response_data, status=status.HTTP_200_OK)