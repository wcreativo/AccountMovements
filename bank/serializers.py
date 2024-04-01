# https://www.django-rest-framework.org/api-guide/serializers/
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from bank.models import Account, AuditClient, Client, Movements

from .utils import inline_serializer


class AuditClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditClient
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    number = serializers.CharField(
        max_length=250, validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = ["current_date"]

    def to_representation(self, instance):
        return super().to_representation(instance)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ["current_date"]
        validators = [
            UniqueTogetherValidator(
                queryset=Client.objects.all(),
                fields=["type_identification", "number_identification"],
            )
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        audit_serializer = AuditClientSerializer(
            AuditClient.objects.filter(client_id=instance.id).order_by("current_date"),
            many=True,
        )
        ret["audit"] = audit_serializer.data
        return ret


class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements
        fields = "__all__"

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    # Solution 5
    def validate_value(self, value):
        if value <= 0:
            raise serializers.ValidationError("Value must be greater that 0")
        return value


# Solution 4
class ClientInlineSerializer(serializers.Serializer):

    type_identification = serializers.CharField()
    number_identification = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    account_set = inline_serializer(
        fields={
            "type": serializers.CharField(),
            "number": serializers.IntegerField(),
            "balance": serializers.CharField(),
        },
        many=True,
    )
