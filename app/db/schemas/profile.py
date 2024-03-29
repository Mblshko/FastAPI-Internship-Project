from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    first_name: str
    last_name: str


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    """Response"""

    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
