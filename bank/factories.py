import random

import factory
from faker import Factory as FakerFactory

from .models import Account, Client, Movements

faker = FakerFactory.create()


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    type_identification = random.choice(["cc", "fc"])
    number_identification = faker.random_int(min=1000000, max=9999999)
    first_name = faker.first_name()
    last_name = faker.last_name()
    birth_date = faker.date_of_birth(minimum_age=18, maximum_age=90)
    current_date = faker.date_time_this_year()


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account


class MovementsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movements
