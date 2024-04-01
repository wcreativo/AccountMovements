# Solution 7
import logging


class AccountUpdater:
    @staticmethod
    def update_balance(account, amount, movement_type):
        if movement_type == "c" or movement_type == "tr":
            account.balance += amount
        elif movement_type == "r" or movement_type == "ts":
            if account.balance - amount < 0:
                raise ValueError(
                    "Transaction cannot be completed! Insufficient balance."
                )
            else:
                account.balance -= amount
                account.balance -= (amount // 1000) * 4

        account.save()

        # Solution 8
        logger = logging.getLogger("balance_changes")
        logger.info(f"Account {account.id} balance updated: {movement_type} {amount}")
