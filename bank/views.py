# https://www.django-rest-framework.org/api-guide/viewsets/
from django.shortcuts import get_object_or_404
from bank.models import Client, Account, Movements
from bank.serializers import ClientSerializer, AccountSerializer, MovementsSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class ClientViewSet(viewsets.ModelViewSet):
    """
    Client API
    ---
    retrieve:
        Return a client instance

    list:
        Return all clients

    create:
        Create a new client

    delete:
        Remove an existing client

    partial_update:
        Update one or more fields on an existing client

    update:
        Update a client
    """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class AccountViewSet(viewsets.ModelViewSet):
    """
    Account API
    ---
    retrieve:
        Return a account instance

    list:
        Return all accounts

    create:
        Create a new account

    delete:
        Remove an existing account

    partial_update:
        Update one or more fields on an existing account

    update:
        Update a account
    """
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def delete(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class MovementsViewSet(viewsets.ModelViewSet):
    """
    Movements API
    ---
    retrieve:
        Return a movement instance

    list:
        Return all movements

    create:
        Create a new movement

    delete:
        Remove an existing movement

    partial_update:
        Update one or more fields on an existing movement

    update:
        Update a movement
    """
    serializer_class = MovementsSerializer
    queryset = Movements.objects.all()

    def create(self, request):
        return super().create(request)

    def update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
