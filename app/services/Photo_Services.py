from sqlalchemy.orm import Session

from app.schemas import PersonCreate
from fastapi import HTTPException
import logging

from forher.app.schemas.Photos import PhotoCreate
from app.core.supabase_client import supabase
from uuid import uuid4
from app.models.Photos import Photo

logger = logging.getLogger(__name__)


def add_photo_services(db: Session, name: str, photo: bytes):
    file_name = f"{uuid4().hex}.jpg"
    file_path = f"photos/{file_name}"

    result = supabase.storage.from_("photos").upload(
        file_path, photo, {"content-type": "image/jpeg"}
    )

    if not result:
        raise HTTPException(status_code=500, detail="Failed to upload photo")

    photo_url = supabase.storage.from_("photos").get_public_url(file_path)

    person = Photo(name=name, photo_url=photo_url)

    db.add(person)
    db.commit()
    db.refresh(person)

    return person


def load_photos_services(db: Session):
    photos = db.query(Photo).order_by(Photo.created_at.desc()).all()

    return photos
