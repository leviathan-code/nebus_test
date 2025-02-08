from app.application.interface.database.repositories.organization_repository import IOrganizationRepository
from app.domain.exceptions import NoResultFoundError
from app.infrastructure.database.models.organization import Organization


class OrganizationInfoByOrganizationIdHandler:
    def __init__(
        self,
        organization_repository: IOrganizationRepository,
    ) -> None:
        self.organization_repository = organization_repository

    async def __call__(
        self,
        organization_id: int,
    ) -> Organization:
        try:
            return await self.organization_repository.get_organization_infoby_organization_id(
                organization_id=organization_id,
            )
        except Exception as e:
            raise NoResultFoundError from e
