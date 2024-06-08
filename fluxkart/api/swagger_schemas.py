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
        example={
            'email': 'example@example.com',
            'phoneNumber': '1234567890'
        }
    ),
    responses={
        201: openapi.Response(
            description="Created or linked contact successfully",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'contact': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'primaryContactId': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'emails': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Items(type=openapi.TYPE_STRING)
                            ),
                            'phoneNumbers': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Items(type=openapi.TYPE_STRING)
                            ),
                            'secondaryContactIds': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Items(type=openapi.TYPE_INTEGER)
                            ),
                        },
                        example={
                            'primaryContactId': 1,
                            'emails': ['primary@example.com', 'secondary@example.com'],
                            'phoneNumbers': ['1234567890', '0987654321'],
                            'secondaryContactIds': [2, 3]
                        }
                    )
                }
            )
        ),
        200: openapi.Response(
            description="Contact already exists",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'contact': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'primaryContactId': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'emails': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Items(type=openapi.TYPE_STRING)
                            ),
                            'phoneNumbers': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Items(type=openapi.TYPE_STRING)
                            ),
                            'secondaryContactIds': openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Items(type=openapi.TYPE_INTEGER)
                            ),
                        },
                        example={
                            'primaryContactId': 1,
                            'emails': ['primary@example.com'],
                            'phoneNumbers': ['1234567890'],
                            'secondaryContactIds': []
                        }
                    )
                }
            )
        ),
    }
)
