from datetime import datetime

from pydantic import BaseModel


class PhotoCreate(BaseModel):
    photo_link: str
    name: str


class PhotoResponse(BaseModel):
    name: str
    photo_url: str
    created_at: datetime

    class Config:
        from_attributes = True
