from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interface.database.uow import IUnitOfWork


class SQLAlchemyBaseUoW(IUnitOfWork):
    """
    Базовый класс UoW (Unit of Work).

    Определяющий логическую транзакцию, т.е. атомарную синхронизацию изменений в объектах.
    Это позволяет слою БЛ управлять транзакциями лично.
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
