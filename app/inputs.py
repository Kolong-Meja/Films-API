# app/inputs.py

import strawberry

from datetime import date, datetime
from typing import Optional

"""
TODO: DEFINE ALL FILM INPUT BELOW!
"""
@strawberry.input(
    description="""Is a Strawberry Input where each field has \
    the same as every field in the Film model.\nNOTE: UUID is excluded from the input\
    It will be generate automatically by it self."""
    )
class FilmCreateInput:
    title: str = strawberry.field(
        description="Title of film data\nNOTE: max length is 255"
        )
    genre: str = strawberry.field(
        description="Genre of film data\nNOTE: max length is 255"
        )
    language: Optional[str] = strawberry.field(
        description="The language options provided by a film\nNOTE: max length is 255"
        )
    release: Optional[date] = strawberry.field(
        default=date.today(),
        description="The release date of a film"
        )
    is_premiere: Optional[bool] = strawberry.field(
        default=False, 
        description="Ensure if the film is already premiered or not."
        )
    timestamp: Optional[datetime] = strawberry.field(
        default=datetime.utcnow(),
        description="Datetime of film data changes", 
        )

@strawberry.input(
    description="""Is a Strawberry Input where each field has \
    the same as every field in the Film model. \
    however, the UUID field is not included""")
class FilmUpdateInput:
    title: Optional[str] = strawberry.field(
        description="Title of film data\nNOTE: max length is 255"
        )
    genre: Optional[str] = strawberry.field(
        description="Genre of film data\nNOTE: max length is 255"
        )
    language: Optional[str] = strawberry.field(
        description="The language options provided by a film\nNOTE: max length is 255"
        )
    release: Optional[date] = strawberry.field(
        default=date.today(),
        description="The release date of a film"
        )
    is_premiere: Optional[bool] = strawberry.field(
        default=False, 
        description="Ensure if the film is already premiered or not."
        )
    timestamp: Optional[datetime] = strawberry.field(
        default=datetime.utcnow(),
        description="Datetime of film data changes", 
        )
    
"""
TODO: DEFINE ALL ACTOR INPUT BELOW!
"""
@strawberry.input(
    description="""Is a Strawberry Input where each field has \
    the same as every field in the Actor model.\nNOTE: UUID is excluded from the input\
    It will be generate automatically by it self."""
    )
class ActorCreateInput:
    name: str = strawberry.field(
        description="Name of the actor or actress.\nNOTE: max length is 255"
        )
    birth_date: Optional[date] = strawberry.field(
        default=date.today(),
        description="Birthdate of the actor or actress",
        )
    biography: Optional[str] = strawberry.field(
        description="Biography of the actor or actress"
        )
    nationality: Optional[str] = strawberry.field(
        description="Nationality of the actor or actress.\nNOTE: max length is 255"
        )
    timestamp: Optional[datetime] = strawberry.field(
        default=datetime.utcnow(),
        description="Datetime of actor data changes.",
        )

@strawberry.input(
    description="""Is a Strawberry Input where each field has \
    the same as every field in the Actor model. \
    however, the UUID field is not included"""
    )
class ActorUpdateInput:
    name: Optional[str] = strawberry.field(
        description="Name of the actor or actress.\nNOTE: max length is 255"
        )
    birth_date: Optional[date] = strawberry.field(
        default=date.today(),
        description="Birthdate of the actor or actress",
        )
    biography: Optional[str] = strawberry.field(
        description="Biography of the actor or actress"
        )
    nationality: Optional[str] = strawberry.field(
        description="Nationality of the actor or actress.\nNOTE: max length is 255"
        )
    timestamp: Optional[datetime] = strawberry.field(
        default=datetime.utcnow(),
        description="Datetime of actor data changes.",
        )

@strawberry.input(
    description="Input for creating connection between Films and Actors table."
    )
class FilmActorInput:
    film_id: str = strawberry.field(
        description="Identifier from Film table\n\
        NOTE: Be careful when input these field, you should take a look first at UUID value in Films table."
        )
    actor_id: str = strawberry.field(
        description="Identifier from Actor table\n\
        NOTE: Be careful when input these field, you should take a look first at UUID value in Actors table."
        )
    timestamp: Optional[datetime] = strawberry.field(
        default=datetime.utcnow(),
        description="Datetime of film actors data changes.",
        )
