from django.db import models
from django.utils.translation import ugettext_lazy as _


class Client(models.Model):
    CITIZENSHIP_CARD = 'cc'
    FOREIGN_CARD = 'fc'
    TYPE_IDENTIFICATIONS = (
        (CITIZENSHIP_CARD, _('citizenship card')),
        (FOREIGN_CARD, _('foreign identity card'))
    )
    type_identification = models.CharField(
        _('type identification'),
        max_length=2,
        choices=TYPE_IDENTIFICATIONS
    )
    number_identification = models.PositiveIntegerField(
        _('number identification'),
    )
    first_name = models.CharField(
        _('first name'),
        max_length=100
    )
    last_name = models.CharField(
        _('last name'),
        max_length=100
    )
    birth_date = models.DateField(
        _('birth date')
    )
    current_date = models.DateTimeField(
        _('current date'),
        auto_now=True
    )

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')
        db_table = "bank_clients"
        indexes = [
            models.Index(fields=['type_identification', 'number_identification'])
        ]


class Account(models.Model):
    SAVING = 's'
    ORDINARY = 'o'
    TYPES = (
        (SAVING, _('saving')),
        (ORDINARY, _('ordinary')),
    )
    client = models.ForeignKey(
        Client,
        verbose_name=_('client'),
        on_delete=models.CASCADE
    )
    type = models.CharField(
        _('type'),
        max_length=1,
        choices=TYPES
    )
    number = models.CharField(
        _('number'),
        max_length=250,
        unique=True
    )
    balance = models.IntegerField(
        _('balance'),
        default=0
    )
    current_date = models.DateTimeField(
        _('current date'),
        auto_now=True
    )

    def __str__(self):
        return f"{self.client} - {self.type}: {self.number}"

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        db_table = "bank_accounts"
        indexes = [
            models.Index(fields=['client'])
        ]


class Movements(models.Model):
    CONSIGNMENT = 'c'
    RETIREMENT = 'r'
    TRANSFER_SEND = 'ts'
    TRANSFER_RECEIVED = 'tr'
    FOUR_PER_ONE_THOUSAND = '4x1000'
    TYPES = (
        (CONSIGNMENT, _('consignment')),
        (RETIREMENT, _('retirement')),
        (FOUR_PER_ONE_THOUSAND, _('4*1000')),
        (TRANSFER_SEND, _('transfer send')),
        (TRANSFER_RECEIVED, _('transfer received')),
    )
    type = models.CharField(
        _('type'),
        max_length=10,
        choices=TYPES
    )
    account = models.ForeignKey(
        Account,
        verbose_name=_('account'),
        on_delete=models.PROTECT
    )
    value = models.DecimalField(
        _('value'),
        decimal_places=2,
        max_digits=15
    )
    current_date = models.DateTimeField(
        _('current date'),
        auto_now=True
    )

    def __str__(self):
        return f"{self.account} - {self.type}: {self.value}"

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        db_table = "bank_accounts_movements"
        indexes = [
            models.Index(fields=['account']),
            models.Index(fields=['account', 'type']),
        ]


class AuditClient(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name=_('client')
    )
    type_identification = models.CharField(
        _('type identification'),
        max_length=2,
    )
    number_identification = models.PositiveIntegerField(
        _('number identification'),
    )
    first_name = models.CharField(
        _('first name'),
        max_length=100
    )
    last_name = models.CharField(
        _('last name'),
        max_length=100
    )
    birth_date = models.DateField(
        _('birth date')
    )
    current_date = models.DateTimeField(
        _('current date'),
        auto_now=True
    )

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = _('audit client')
        verbose_name_plural = _('audits clients')
        db_table = "audit_clients"
        indexes = [
            models.Index(fields=['client'])
        ]
