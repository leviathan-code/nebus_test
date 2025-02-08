from geoalchemy2 import Geometry
from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models.base import BaseModel


class Building(BaseModel):
    __tablename__ = "building"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    adress: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    geo_coords = Column(Geometry("POINT", srid=4326))
