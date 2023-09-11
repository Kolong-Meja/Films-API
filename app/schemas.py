# app/schemas.py

from uuid import uuid4 as uuid
from datetime import datetime, date
from pydantic import (
    BaseModel, 
    ConfigDict,
    Field,
    )
from typing import Optional, List


"""
TODO: Create schemas
"""

# create Film base model
class FilmBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    uuid: str = Field(
        default_factory=lambda: uuid().hex,
        title="UUID", 
        description="Identifier for film data", 
        max_length=36
        )
    title: str = Field(
        title="Title", 
        description="Title of the film", 
        max_length=255
        )
    genre: str = Field(
        title="Genre", 
        description="Genre of the film.", 
        max_length=255
        )
    language: str = Field(
        title="Language",
        description="The language options provided by a film",
        max_length=255
        )
    release: Optional[date] = Field(
        default=date(year=2011, month=1, day=1),
        title="Release of the date",
        description="The release date of a film"
        )
    is_premiere: bool = Field(
        default=False, 
        title="Is Premiere", 
        description="Descript whether the film is premiered or not"
        )
    timestamp: datetime = Field(
        default=datetime.now(),
        title="Timestamp", 
        description="Datetime of film data changes"
        )

class FilmUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: Optional[str] = Field(
        default=None,
        title="Title", 
        description="Title of the film", 
        max_length=255
        )
    genre: Optional[str] = Field(
        default=None,
        title="Genre", 
        description="Genre of the film.", 
        max_length=255
        )
    language: Optional[str] = Field(
        title="Language",
        description="The language options provided by a film",
        max_length=255
        )
    release: Optional[date] = Field(
        default=date(year=2011, month=1, day=1),
        title="Release of the date",
        description="The release date of a film"
        )
    is_premiere: Optional[bool] = Field(
        default=False, 
        title="Is Premiere", 
        description="Descript whether the film is premiered or not"
        )
    timestamp: Optional[datetime] = Field(
        default=datetime.now(),
        title="Timestamp", 
        description="Datetime of film data changes"
        )

# create Actor base model
class ActorBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    uuid: str = Field(
        default_factory=lambda: uuid().hex,
        title="UUID",
        description="Identifier for actor data",
        max_length=36
        )
    name: str = Field(
        title="Name",
        description="The name of the actor",
        max_length=255
        )
    birth_date: Optional[date] = Field(
        default=date.today(),
        title="Birthdate",
        description="The birth date of the actors",
        )
    biography: Optional[str] = Field(
        title="Biography",
        description="Biography from the actor",
        )
    nationality: Optional[str] = Field(
        title="Nationality",
        description="The nationality of actor",
        max_length=255
        )
    timestamp: Optional[datetime] = Field(
        default=datetime.utcnow(),
        title="Timestamp",
        description="Datetime of actor data changes."
        )

class ActorUpdateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = Field(
        title="Name",
        description="The name of the actor",
        max_length=255
        )
    birth_date: Optional[date] = Field(
        default=date.today(),
        title="Birthdate",
        description="The birth date of the actors",
        )
    biography: Optional[str] = Field(
        title="Biography",
        description="Biography from the actor",
        )
    nationality: Optional[str] = Field(
        title="Nationality",
        description="The nationality of actor",
        max_length=255
        )
    timestamp: Optional[datetime] = Field(
        default=datetime.utcnow(),
        title="Timestamp",
        description="Datetime of actor data changes."
        )

class FilmActorBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    uuid: str = Field(
        default_factory=lambda: uuid().hex,
        title="UUID",
        description="Identifier for film actors data",
        )
    film_id: str = Field(
        title="Film ID",
        description="Identifier for film data"
        )
    actor_id: str = Field(
        title="Actor ID",
        description="Identifier for actor data"
        )
    timestamp: datetime = Field(
        default=datetime.utcnow(),
        title="Timestamp",
        description="Datetime of film actors data changes"
        )

class FilmSchema(FilmBase):
    actors: List[ActorBase]

class ActorSchema(ActorBase):
    films: List[FilmBase]

class FilmActorSchema(FilmActorBase):
    pass

