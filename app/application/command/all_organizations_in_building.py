from collections.abc import Sequence

from sqlalchemy.exc import SQLAlchemyError

from app.application.interface.database.repositories.organization_repository import IOrganizationRepository
from app.domain.exceptions import NoResultFoundError
from app.infrastructure.database.models.organization import Organization


class AllOrganizationsInBuildingHandler:
    def __init__(
        self,
        organization_repository: IOrganizationRepository,
    ) -> None:
        self.organization_repository = organization_repository

    async def __call__(
        self,
        building_id: int,
    ) -> Sequence[Organization]:
        try:
            return await self.organization_repository.get_all_buildings_by_building_id(
                building_id=building_id,
            )
        except SQLAlchemyError as e:
            raise NoResultFoundError from e
