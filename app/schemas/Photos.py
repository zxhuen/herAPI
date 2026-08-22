from pydantic import BaseModel


class PhotoCreate(BaseModel):
    photo_link: str
    name: str
