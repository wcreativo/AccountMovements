from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BankConfig(AppConfig):
    name = 'bank'
    verbose_name = _('bank')

    def ready(self):
        import bank.signals
