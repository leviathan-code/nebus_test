from collections.abc import AsyncIterable, Iterable

from dishka import Provider, Scope, provide
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from app.settings.database.database_settings import DatabaseSettings


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_engine(self, config: DatabaseSettings) -> AsyncIterable[AsyncEngine]:
        engine = create_async_engine(
            config.dsn(),
            echo=False,
        )
        yield engine
        await engine.dispose(close=True)

    @provide(scope=Scope.APP)
    def get_sync_engine(self, config: DatabaseSettings) -> Iterable[Engine]:
        engine = create_engine(
            config.dsn(),
        )
        yield engine
        engine.dispose(close=True)

    @provide(scope=Scope.APP)
    def get_async_pool(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def get_session(
        self,
        pool: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[AsyncSession]:
        async with pool() as session:
            yield session
