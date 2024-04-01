from django.test import TestCase

from .models import Account
from .services import AccountUpdater


class TestAccountUpdater(TestCase):
    def setUp(self):
        self.account = Account.objects.create(balance=10000)

    def test_deposit(self):
        AccountUpdater.update_balance(self.account, 2000, "c")
        self.assertEqual(self.account.balance, 12000)

    def test_withdrawal_sufficient_balance(self):
        AccountUpdater.update_balance(self.account, 5000, "r")
        self.assertEqual(self.account.balance, 6980)

    def test_withdrawal_insufficient_balance(self):
        with self.assertRaises(ValueError):
            AccountUpdater.update_balance(self.account, 15000, "r")

    def test_transfer_sent_sufficient_balance(self):
        AccountUpdater.update_balance(self.account, 3000, "ts")
        self.assertEqual(self.account.balance, 3968)

    def test_transfer_sent_insufficient_balance(self):
        with self.assertRaises(ValueError):
            AccountUpdater.update_balance(self.account, 10000, "ts")
