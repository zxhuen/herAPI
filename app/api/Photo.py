from fastapi import APIRouter, Request, UploadFile, Form, File, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas import PersonCreate, PersonResponse
from app.services import (
    add_person_services,
    list_person_services,
    edit_person_services,
    delete_person_services,
)
from app.core.limiter import limiter
from app.services.Photo_Services import add_photo_services, load_photos_services
from app.schemas.Photos import PhotoResponse

router = APIRouter(prefix="/Photo", tags=["Photo"])


@router.post("/add-photo")
@limiter.limit("10/minute")
def add_photo(
    request: Request,
    name: str = Form(...),
    photo: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    photo_bytes = photo.file.read()

    return add_photo_services(db, name, photo_bytes)


@router.get("/load-photo", response_model=list[PhotoResponse])
@limiter.limit("10/minute")
def load_photo(request: Request, db: Session = Depends(get_db)):
    return load_photos_services(db)
