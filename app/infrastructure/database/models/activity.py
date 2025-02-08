from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database.models.base import BaseModel


class Activity(BaseModel):
    __tablename__ = "activity"

    name: Mapped[str] = mapped_column(String, nullable=False)
    parent_activity_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("activity.id"),
        nullable=True,
    )

    children_activity = relationship(
        "Activity",
        lazy="joined",
        join_depth=3,
    )
    organization: Mapped[list["Organization"]] = relationship(  # noqa: F821
        secondary="activity_organization",
        back_populates="activity",
    )


class ActivityOrganization(BaseModel):
    __tablename__ = "activity_organization"

    activity_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("activity.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    organization_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("organization.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
