from pydantic import BaseModel


class OrganizationSchema(BaseModel):
    name: str
    mobile_phone: list[str]
    adress: str
    activity: list[str]
