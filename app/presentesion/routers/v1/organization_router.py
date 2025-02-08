from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from app.application.command.all_organizations_by_points import AllOrganizationsByPointsHandler, Point
from app.application.command.all_organizations_in_activity import AllOrganizationsInActivityHandler
from app.application.command.all_organizations_in_building import AllOrganizationsInBuildingHandler
from app.application.command.organization_by_name import OrganizationByNameyHandler
from app.application.command.organization_info_by_organization_id import (
    OrganizationInfoByOrganizationIdHandler,
)
from app.application.command.organizations_by_activity import OrganizationsByActivityHandler
from app.presentesion.routers.schemas import OrganizationSchema

router = APIRouter(prefix="/organization", route_class=DishkaRoute, tags=["Organization"])


@router.get(
    path="/organizations-in-building/{building_id}",
    response_model=list[OrganizationSchema],
)
async def get_all_organizations_in_building(
    building_id: int,
    interactor: FromDishka[AllOrganizationsInBuildingHandler],
) -> list[OrganizationSchema]:
    return [
        OrganizationSchema(
            name=organization.name,
            mobile_phone=organization.mobile_phone,
            adress=organization.building.adress,
            activity=[activity.name for activity in organization.activity],
        )
        for organization in await interactor(building_id=building_id)
    ]


@router.get(
    path="/organizations-in-activity/{activity_id}",
    response_model=list[OrganizationSchema],
)
async def get_all_organizations_in_activity(
    activity_id: int,
    interactor: FromDishka[AllOrganizationsInActivityHandler],
) -> list[OrganizationSchema]:
    return [
        OrganizationSchema(
            name=organization.name,
            mobile_phone=organization.mobile_phone,
            adress=organization.building.adress,
            activity=[activity.name for activity in organization.activity],
        )
        for organization in await interactor(activity_id=activity_id)
    ]


@router.get(
    path="/organizations-by-points/",
    response_model=list[OrganizationSchema],
)
async def get_all_organizations_by_points(
    latitude: float,
    longitude: float,
    radius: int,
    interactor: FromDishka[AllOrganizationsByPointsHandler],
) -> list[OrganizationSchema]:
    return [
        OrganizationSchema(
            name=organization.name,
            mobile_phone=organization.mobile_phone,
            adress=organization.building.adress,
            activity=[activity.name for activity in organization.activity],
        )
        for organization in await interactor(
            command_data=Point(
                latitude=latitude,
                longitude=longitude,
                radius=radius,
            ),
        )
    ]


@router.get(
    path="/organization-info/{organization_id}",
    response_model=OrganizationSchema,
)
async def get_organization_info_by_organization_id(
    organization_id: int,
    interactor: FromDishka[OrganizationInfoByOrganizationIdHandler],
) -> OrganizationSchema:
    organization = await interactor(organization_id=organization_id)
    return OrganizationSchema(
        name=organization.name,
        mobile_phone=organization.mobile_phone,
        adress=organization.building.adress,
        activity=[activity.name for activity in organization.activity],
    )


@router.get(
    path="/organizations-by-activity",
    response_model=list[OrganizationSchema],
)
async def get_organizations_by_activity(
    activity_name: str,
    interactor: FromDishka[OrganizationsByActivityHandler],
) -> list[OrganizationSchema]:
    return [
        OrganizationSchema(
            name=organization.name,
            mobile_phone=organization.mobile_phone,
            adress=organization.building.adress,
            activity=[activity.name for activity in organization.activity],
        )
        for organization in await interactor(activity_name=activity_name)
    ]


@router.get(
    path="/organization-by-name",
    response_model=OrganizationSchema,
)
async def get_organization_by_name(
    name: str,
    interactor: FromDishka[OrganizationByNameyHandler],
) -> OrganizationSchema:
    organization = await interactor(name=name)
    return OrganizationSchema(
        name=organization.name,
        mobile_phone=organization.mobile_phone,
        adress=organization.building.adress,
        activity=[activity.name for activity in organization.activity],
    )
