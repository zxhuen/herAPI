from sqlalchemy.orm import Session

from app.schemas import PersonCreate
from fastapi import HTTPException
import logging

from forher.app.schemas.Photos import PhotoCreate

logger = logging.getLogger(__name__)


def add_person_services(db: Session, name: str, photo: bytes):
    


