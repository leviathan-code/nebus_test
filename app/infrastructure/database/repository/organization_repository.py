from collections.abc import Sequence

from geoalchemy2.functions import ST_DWithin
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.application.interface.database.repositories.organization_repository import IOrganizationRepository
from app.infrastructure.database.models.activity import Activity
from app.infrastructure.database.models.building import Building
from app.infrastructure.database.models.organization import Organization
from app.infrastructure.database.repository.base import SQLAlchemyRepository


class OrganizationRepository(IOrganizationRepository, SQLAlchemyRepository):
    async def get_all_buildings_by_building_id(
        self,
        building_id: int,
    ) -> Sequence[Organization]:
        query = (
            select(Organization)
            .options(
                joinedload(Organization.building),
                joinedload(Organization.activity),
            )
            .where(Organization.building_id == building_id)
        )
        result = await self._session.execute(query)
        return result.unique().scalars().all()

    async def get_all_organizations_in_activity(
        self,
        activity_id: int,
    ) -> Sequence[Organization]:
        query = (
            select(Organization)
            .options(
                joinedload(Organization.building),
                joinedload(Organization.activity),
            )
            .where(Activity.id == activity_id)
        )
        result = await self._session.execute(query)
        return result.unique().scalars().all()

    async def get_all_organizations_by_point(
        self,
        latitude: float,
        longitude: float,
        radius: int,
    ) -> Sequence[Organization]:
        query = (
            select(Organization)
            .options(
                joinedload(Organization.building),
                joinedload(Organization.activity),
            )
            .where(
                ST_DWithin(
                    Building.geo_coords,
                    f"SRID=4326;POINT({latitude} {longitude})",
                    radius,
                ),
            )
        )
        result = await self._session.execute(query)
        return result.unique().scalars().all()

    async def get_organization_infoby_organization_id(
        self,
        organization_id: int,
    ) -> Organization:
        query = (
            select(Organization)
            .options(
                joinedload(Organization.building),
                joinedload(Organization.activity),
            )
            .where(Organization.id == organization_id)
        )
        result = await self._session.execute(query)
        return result.unique().scalar_one()

    async def get_organizations_by_activity(
        self,
        activity_name: str,
    ) -> Sequence[Organization]:
        query = (
            select(Organization)
            .options(
                joinedload(Organization.building),
                joinedload(Organization.activity),
            )
            .filter(Activity.name == activity_name)
        )
        result = await self._session.execute(query)
        return result.unique().scalars().all()

    async def get_organization_by_name(
        self,
        name: str,
    ) -> Organization:
        query = (
            select(Organization)
            .options(
                joinedload(Organization.building),
                joinedload(Organization.activity),
            )
            .where(Organization.name.like(name))
        )
        result = await self._session.execute(query)
        return result.unique().scalar_one()
