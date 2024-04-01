from pytest_factoryboy import register

from ..factories import AccountFactory, ClientFactory, MovementsFactory

register(ClientFactory)
register(MovementsFactory)
register(AccountFactory)
