from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bank.views import ClientViewSet, AccountViewSet, MovementsViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'movements', MovementsViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('bank/', include(router.urls)),
]