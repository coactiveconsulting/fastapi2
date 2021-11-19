from fastapi.params import Depends
from .. import models, schemas, utils
from fastapi import FastAPI, Response, responses, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_users(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    response_model=schemas.UserOut,
):
    # hash the password
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# retrieve a particular user
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()
    print(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with {id} was not found",
        )

    return user
