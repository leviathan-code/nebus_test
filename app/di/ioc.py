from dishka import Provider, Scope, provide

from app.application.command.all_organizations_by_points import AllOrganizationsByPointsHandler
from app.application.command.all_organizations_in_activity import AllOrganizationsInActivityHandler
from app.application.command.all_organizations_in_building import AllOrganizationsInBuildingHandler
from app.application.command.organization_by_name import OrganizationByNameyHandler
from app.application.command.organization_info_by_organization_id import (
    OrganizationInfoByOrganizationIdHandler,
)
from app.application.command.organizations_by_activity import OrganizationsByActivityHandler
from app.application.interface.database.repositories.organization_repository import IOrganizationRepository


class InteractorProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_all_buildings_by_building_id_handler(
        self,
        organization_repository: IOrganizationRepository,
    ) -> AllOrganizationsInBuildingHandler:
        return AllOrganizationsInBuildingHandler(
            organization_repository=organization_repository,
        )

    @provide(scope=Scope.REQUEST)
    def get_all_organizations_in_activity_handler(
        self,
        organization_repository: IOrganizationRepository,
    ) -> AllOrganizationsInActivityHandler:
        return AllOrganizationsInActivityHandler(
            organization_repository=organization_repository,
        )

    @provide(scope=Scope.REQUEST)
    def get_all_organizations_by_point_handler(
        self,
        organization_repository: IOrganizationRepository,
    ) -> AllOrganizationsByPointsHandler:
        return AllOrganizationsByPointsHandler(
            organization_repository=organization_repository,
        )

    @provide(scope=Scope.REQUEST)
    def get_organization_info_handler(
        self,
        organization_repository: IOrganizationRepository,
    ) -> OrganizationInfoByOrganizationIdHandler:
        return OrganizationInfoByOrganizationIdHandler(
            organization_repository=organization_repository,
        )

    @provide(scope=Scope.REQUEST)
    def get_organizations_by_activity_handler(
        self,
        organization_repository: IOrganizationRepository,
    ) -> OrganizationsByActivityHandler:
        return OrganizationsByActivityHandler(
            organization_repository=organization_repository,
        )

    @provide(scope=Scope.REQUEST)
    def get_organization_by_name_handler(
        self,
        organization_repository: IOrganizationRepository,
    ) -> OrganizationByNameyHandler:
        return OrganizationByNameyHandler(
            organization_repository=organization_repository,
        )
