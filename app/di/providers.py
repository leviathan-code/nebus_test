from collections.abc import Iterable

from dishka import Provider

from app.di.config import ConfigProvider
from app.di.database import DatabaseProvider
from app.di.ioc import InteractorProvider
from app.di.repository import RepositoriesProvider
from app.di.uow import UoWProvider


def make_providers() -> Iterable[Provider]:
    return (
        ConfigProvider(),
        InteractorProvider(),
        UoWProvider(),
        RepositoriesProvider(),
        DatabaseProvider(),
    )
