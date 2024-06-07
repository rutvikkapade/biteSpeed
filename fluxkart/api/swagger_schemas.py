from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

create_contact_schema = swagger_auto_schema(
    operation_description="Create a new contact or link an existing contact",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address of the contact'),
            'phoneNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number of the contact'),
        },
        required=['email', 'phoneNumber'],
    ),
    responses={
        201: openapi.Response(
            description="Created or linked contact successfully",
            examples={
                "application/json": {
                    "contact": {
                        "primaryContactId": 1,
                        "emails": ["primary@example.com", "secondary@example.com"],
                        "phoneNumbers": ["1234567890", "0987654321"],
                        "secondaryContactIds": [2, 3]
                    }
                }
            }
        ),
        200: openapi.Response(
            description="Contact already exists",
            examples={
                "application/json": {
                    "contact": {
                        "primaryContactId": 1,
                        "emails": ["primary@example.com"],
                        "phoneNumbers": ["1234567890"],
                        "secondaryContactIds": []
                    }
                }
            }
        ),
    }
)
