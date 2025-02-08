import http

from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError


class NoResultFoundError(SQLAlchemyError): ...


async def object_not_found_error_handler(_: Request, exc: NoResultFoundError) -> JSONResponse:
    return JSONResponse(content={"message": "Объект не найден"}, status_code=http.HTTPStatus.NOT_FOUND)


async def internal_error_handler(_: Request, exc: NoResultFoundError) -> JSONResponse:
    return JSONResponse(
        content={"message": "Ошибка сервера"},
        status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
    )
