# app/types.py

import strawberry

from app.schemas import (
    FilmBase as film_base,
    ActorBase as actor_base,
    FilmSchema as film_schema,
    ActorSchema as actor_schema,
    FilmUpdateSchema as film_update_schema,
    ActorUpdateSchema as actor_update_schema,
    FilmActorSchema as film_actor_schema,
    )
from typing import Any


"""
NOTE: Define model base type.
"""
# define FilmTypeBase basic schema
@strawberry.experimental.pydantic.type(
    model=film_base,
    description="""is the base of the Film schema, \
    this is useful for using relationships between Film models and Actor""",
    all_fields=True
    )
class FilmTypeBase:
    pass

# define ActorTypeBase basic schema
@strawberry.experimental.pydantic.type(
    model=actor_base,
    description="""Is the base of the Actor schema, \
    this is useful for using relationships between Actor models and Films""",
    all_fields=True
    )
class ActorTypeBase:
    pass

"""
TODO: DEFINE ALL FILM TYPE BELOW!
"""
# define FilmType basic schema
@strawberry.experimental.pydantic.type(
    model=film_schema,
    description="Is a Film model but wrapped in Strawberry Type",
    all_fields=True
    )
class FilmType:
    pass

@strawberry.experimental.pydantic.type(
    model=film_update_schema,
    description="""This is the type for updating film data"""
    )
class FilmUpdateType:
    title: strawberry.auto = strawberry.UNSET
    genre: strawberry.auto = strawberry.UNSET
    language: strawberry.auto = strawberry.UNSET
    release: strawberry.auto = strawberry.UNSET
    is_premiere: strawberry.auto = strawberry.UNSET
    timestamp: strawberry.auto = strawberry.UNSET

"""
TODO: DEFINE ALL ACTOR TYPE BELOW!
"""
@strawberry.experimental.pydantic.type(
    model=actor_schema,
    description="Is a Actor model but wrapped in Strawberry Type",
    all_fields=True
    )
class ActorType:
    pass

@strawberry.experimental.pydantic.type(
    model=actor_update_schema,
    description="""This is the type for updating actor data"""
    )
class ActorUpdateType:
    name: strawberry.auto = strawberry.UNSET
    birth_date: strawberry.auto = strawberry.UNSET
    biography: strawberry.auto = strawberry.UNSET
    nationality: strawberry.auto = strawberry.UNSET
    timestamp: strawberry.auto = strawberry.UNSET

@strawberry.experimental.pydantic.type(
    model=film_actor_schema,
    description="""Is the base of the Film Actors schema, \
    this is useful for using relationships between Actor models and Films""",
    all_fields=True
    )
class FilmActorTypeBase:
    pass

"""
TODO: DEFINE ALL RESPONSE TYPE BELOW!
"""
# use for return success response.
@strawberry.type(
    description="Representation of the successful response."
    )
class Response:
    message: str = strawberry.field(
        description="Use for return a response"
        )

# combine film data with response.
@strawberry.type(
    description="""Is a combination between film data with response data."""
    )
class FilmCreateResponse:
    film: FilmTypeBase
    response: Response

@strawberry.type(
    description="""Is a combination between film data with response data."""
    )
class FilmUpdateResponse:
    film: FilmUpdateType
    response: Response

# combine actor data with response.
@strawberry.type(
    description="""Is a combination between actor data with response data."""
    )
class ActorCreateResponse:
    actor: ActorTypeBase
    response: Response

@strawberry.type(
    description="""Is a combination between actor data with response data."""
    )
class ActorUpdateResponse:
    actor: ActorUpdateType
    response: Response

@strawberry.type(
    description="""Is a combination between film actors data with response data."""
    )
class FilmActorResponse:
    film_actor: FilmActorTypeBase
    response: Response

