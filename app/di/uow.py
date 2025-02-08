from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interface.database.uow import IUnitOfWork
from app.infrastructure.database.uow.base import UnitOfWork
from app.infrastructure.database.uow.uow import SQLAlchemyBaseUoW


class UoWProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_uow(self, session: AsyncSession) -> IUnitOfWork:
        db_uow = SQLAlchemyBaseUoW(session=session)
        return UnitOfWork((db_uow,))
