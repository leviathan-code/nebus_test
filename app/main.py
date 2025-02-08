from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import APIRouter, FastAPI

from app.di.providers import make_providers
from app.domain.exceptions import NoResultFoundError, internal_error_handler, object_not_found_error_handler
from app.presentesion.routers.v1.organization_router import router as api_v1_router
from app.settings.factory import SettingsFactory

config = SettingsFactory()


def create_di_container() -> AsyncContainer:
    return make_async_container(*make_providers())


def create_app() -> FastAPI:
    application = FastAPI()
    api_v1 = APIRouter(prefix="/api/v1")
    api_v1.include_router(api_v1_router)
    application.include_router(api_v1)
    application.add_exception_handler(NoResultFoundError, object_not_found_error_handler)
    application.add_exception_handler(Exception, internal_error_handler)

    container = create_di_container()
    setup_dishka(container, application)

    return application


app = create_app()
