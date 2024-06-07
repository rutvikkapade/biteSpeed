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
            else:
                if existing_contact_by_email.id<existing_contact_by_phone.id:
                    existing_contact_by_phone.linkPrecedence = 'secondary'
                    if existing_contact_by_email.linkPrecedence == 'secondary':
                        primary_contact = existing_contact_by_email.linkedId
                    else:
                        primary_contact = existing_contact_by_email
                    existing_contact_by_phone.linkedId = primary_contact
                    existing_contact_by_phone.save()
                else:
                    existing_contact_by_email.linkPrecedence = 'secondary'
                    if existing_contact_by_phone.linkPrecedence == 'secondary':
                        primary_contact = existing_contact_by_phone.linkedId
                    else:
                        primary_contact = existing_contact_by_phone
                    existing_contact_by_email.linkedId = primary_contact
                    existing_contact_by_email.save()
                response_data = self.build_response(primary_contact)
                return Response(response_data, status=status.HTTP_200_OK)
        if not existing_contact_by_email and not existing_contact_by_phone:
            # If neither email nor phone number exist, add a new primary contact
            primary_contact = Contact.objects.create(
                email=email,
                phoneNumber=phoneNumber,
                linkPrecedence='primary',
            )
        else:
            # Otherwise, add a new secondary contact linked to the existing primary contact
            primary_contact = existing_contact_by_email or existing_contact_by_phone
            if primary_contact.linkPrecedence == 'secondary':
                linkedId=primary_contact.linkedId
            else:
                linkedId=primary_contact
            Contact.objects.create(
                    email=email,
                    phoneNumber=phoneNumber,
                    linkedId = linkedId,
                    linkPrecedence='secondary'
                )


        response_data = self.build_response(primary_contact)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def build_response(self, primary_contact):
        secondary_contacts = Contact.objects.filter(linkedId = primary_contact)
        emails = [primary_contact.email]
        phoneNumbers = [primary_contact.phoneNumber]
        [emails.append(contact.email) for contact in secondary_contacts if contact.email not in emails]
        [phoneNumbers.append(contact.phoneNumber) for contact in secondary_contacts if contact.phoneNumber not in phoneNumbers]
        secondary_contact_ids = [contact.id for contact in secondary_contacts]

        response_data = {
            "contact": {
                "primaryContactId": primary_contact.id,
                "emails": emails,
                "phoneNumbers": phoneNumbers,
                "secondaryContactIds": secondary_contact_ids
            }
        }
        return response_data
