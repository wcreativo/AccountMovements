import django_filters

from .models import Account, Client, Movements


class ClientFilter(django_filters.FilterSet):
    number_identification = django_filters.NumberFilter()

    class Meta:
        model = Client
        fields = ["number_identification"]


class AccountFitler(django_filters.FilterSet):
    client__number_identification = django_filters.NumberFilter()

    class Meta:
        model = Account
        fields = ["client__number_identification"]


class MovementsFilter(django_filters.FilterSet):
    account__number = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Movements
        fields = ["account__number"]
