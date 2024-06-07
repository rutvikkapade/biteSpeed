from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Setup the schema view for Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Contact API",
      default_version='v1',
      description="API documentation for the Contact app",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'identify', ContactViewSet, basename='contact')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
