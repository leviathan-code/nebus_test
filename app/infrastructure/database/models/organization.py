from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.models.base import BaseModel
from app.infrastructure.database.models.building import Building


class Organization(BaseModel):
    __tablename__ = "organization"

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    mobile_phone: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        nullable=False,
    )
    building_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("building.id", ondelete="CASCADE"),
        nullable=False,
    )

    building: Mapped[Building] = relationship()
    activity: Mapped[list["Activity"]] = relationship(  # noqa: F821
        secondary="activity_organization",
        back_populates="organization",
    )
