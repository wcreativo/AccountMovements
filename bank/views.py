# https://www.django-rest-framework.org/api-guide/viewsets/
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from bank.models import Account, Client, Movements
from bank.serializers import (AccountSerializer, ClientInlineSerializer,
                              ClientSerializer, MovementsSerializer)
from bank.services import AccountUpdater


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

    queryset = Client.objects.all()

    # Solution 4
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ClientSerializer
        return ClientSerializer


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

    # Solution 7
    @transaction.atomic
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        account = serializer.validated_data["account"]
        amount = serializer.validated_data["value"]
        movement_type = serializer.validated_data["type"]

        AccountUpdater.update_balance(account, amount, movement_type)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
