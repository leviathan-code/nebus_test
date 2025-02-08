from collections.abc import Sequence
from dataclasses import dataclass

from sqlalchemy.exc import SQLAlchemyError

from app.application.interface.database.repositories.organization_repository import IOrganizationRepository
from app.domain.exceptions import NoResultFoundError
from app.infrastructure.database.models.organization import Organization


@dataclass
class Point:
    latitude: float
    longitude: float
    radius: int


class AllOrganizationsByPointsHandler:
    def __init__(
        self,
        organization_repository: IOrganizationRepository,
    ) -> None:
        self.organization_repository = organization_repository

    async def __call__(
        self,
        command_data: Point,
    ) -> Sequence[Organization]:
        try:
            return await self.organization_repository.get_all_organizations_by_point(
                latitude=command_data.latitude,
                longitude=command_data.longitude,
                radius=command_data.radius,
            )
        except SQLAlchemyError as e:
            raise NoResultFoundError from e
