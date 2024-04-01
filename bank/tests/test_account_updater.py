import pytest
from django.test import TestCase

from bank.models import Account
from bank.services import AccountUpdater

from ..factories import AccountFactory, ClientFactory, MovementsFactory

pytestmark = pytest.mark.django_db


class TestAccountUpdater(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = ClientFactory()
        cls.account = AccountFactory(client=cls.client, balance=10000)

    def test_deposit(self):
        AccountUpdater.update_balance(self.account, 2000, "c")
        self.assertEqual(self.account.balance, 12000)

    def test_withdrawal_sufficient_balance(self):
        AccountUpdater.update_balance(self.account, 5000, "r")
        self.assertEqual(self.account.balance, 6980)

    def test_withdrawal_insufficient_balance(self):
        with self.assertRaises(ValueError):
            AccountUpdater.update_balance(self.account, 15000, "r")
