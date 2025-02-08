from abc import ABC, abstractmethod
from collections.abc import Sequence

from app.infrastructure.database.models.organization import Organization


class IOrganizationRepository(ABC):
    @abstractmethod
    async def get_all_buildings_by_building_id(
        self,
        building_id: int,
    ) -> Sequence[Organization]:
        raise NotImplementedError

    @abstractmethod
    async def get_all_organizations_in_activity(
        self,
        activity_id: int,
    ) -> Sequence[Organization]:
        raise NotImplementedError

    @abstractmethod
    async def get_all_organizations_by_point(
        self,
        latitude: float,
        longitude: float,
        radius: int,
    ) -> Sequence[Organization]:
        raise NotImplementedError

    @abstractmethod
    async def get_organization_infoby_organization_id(
        self,
        organization_id: int,
    ) -> Organization:
        raise NotImplementedError

    @abstractmethod
    async def get_organizations_by_activity(
        self,
        activity_name: str,
    ) -> Sequence[Organization]:
        raise NotImplementedError

    @abstractmethod
    async def get_organization_by_name(
        self,
        name: str,
    ) -> Organization:
        raise NotImplementedError
