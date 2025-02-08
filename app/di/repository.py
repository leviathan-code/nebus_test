from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interface.database.repositories.organization_repository import IOrganizationRepository
from app.infrastructure.database.repository.organization_repository import OrganizationRepository


class RepositoriesProvider(Provider):
    @provide(scope=Scope.REQUEST, provides=IOrganizationRepository)
    def get_organization_repository(self, session: AsyncSession) -> OrganizationRepository:
        return OrganizationRepository(session)
