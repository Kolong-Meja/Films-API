# app/query.py

import strawberry
import json

from strawberry.types import Info as type_info
from app.models import (
    Film as film_model,
    Actor as actor_model,
    FilmActor as film_actor_model,
    )
from app.types import (
    FilmTypeBase as film_type_base,
    ActorTypeBase as actor_type_base,
    FilmActorTypeBase as film_actor_type_base,
    FilmType as film_type,
    ActorType as actor_type,
    )
from app.config import SessionLocal as session_local
from sqlalchemy import and_
from sqlalchemy.orm import joinedload
from app.schemas import FilmSchema as film_schema
from pydantic.json_schema import model_json_schema
from typing import Optional


"""
TODO: Define main Query class BELOW!
"""
# define Query main schema
@strawberry.type(
    description="""Is a command to get a lot of data from the server. \
    This is almost similar to using SELECT FROM statement in SQL, but only not like SQL"""
    )
class Query:
    @strawberry.field(
        description="Useful for fetching a list of movies from the server"
        )
    # get all films data from database.
    def get_films(uuid: str = "", next: bool = False, limit: int = 10) -> list[film_type_base]:
        with session_local() as session:
            if uuid != "" and next:
                films = session.query(film_model).where(film_model.uuid > uuid).order_by(film_model.uuid).limit(limit).all()
            elif uuid != "" and not next:
                films = session.query(film_model).where(film_model.uuid < uuid).order_by(film_model.uuid.desc()).limit(limit).all()
            else:
                films = session.query(film_model).order_by(film_model.uuid).limit(limit).all()

            if not films:
                raise Exception("Data not found or empty.")
            
            return [film_type_base(
                uuid=film.uuid,
                title=film.title,
                genre=film.genre,
                language=film.language,
                release=film.release,
                is_premiere=film.is_premiere,
                timestamp=film.timestamp,
            ) for film in films]
    
    @strawberry.field(
        description="""Useful for retrieving single movie data from the server. \
        To carry out this command, you need to enter the title argument, \
        which determines whether a film with the same title is recorded on the server or not."""
        )
    # get one film data from database.
    def get_film(info: type_info, title: str, film_id: Optional[str] = None) -> film_type_base:
        with session_local() as session:
            if film_id is not None:
                film = session.query(film_model).where(and_(film_model.title == title, film_model.uuid == film_id)).first()

                if not film:
                    raise Exception(f"Film '{title}' or ID '{film_id}' not found.")
            else:
                film = session.query(film_model).filter(film_model.title == title).first()

                if not film:
                    raise Exception(f"Film '{title}' not found.")

            return film_type_base(
                uuid=film.uuid,
                title=film.title,
                genre=film.genre,
                language=film.language,
                release=film.release,
                is_premiere=film.is_premiere,
                timestamp=film.timestamp
            )

    @strawberry.field(
        description="""This is useful for retrieving Actor data from the server. \
        Usage can be done by limiting the amount of data retrieved."""
        )
    def get_actors(uuid: str = "", next: bool = False, limit: int = 10) -> list[actor_type_base]:
        with session_local() as session:
            if uuid != "" and next:
                actors = session.query(actor_model).where(actor_model.uuid > uuid).order_by(actor_model.uuid).limit(limit).all()
            elif uuid != "" and not next:
                actors = session.query(actor_model).where(actor_model.uuid < uuid).order_by(actor_model.uuid.desc()).limit(limit).all()
            else:
                actors = session.query(actor_model).order_by(actor_model.uuid).limit(limit).all()

            if not actors:
                raise Exception("Data not found or empty.")
        
            return [actor_type_base(
                uuid=actor.uuid,
                name=actor.name,
                birth_date=actor.birth_date,
                biography=actor.biography,
                nationality=actor.nationality,
                timestamp=actor.timestamp
            ) for actor in actors]

    @strawberry.field(
        description="""This is useful for retrieving a single Actor data from the server. \
        If the name argument does not have the same data in the "name" field in the Actor table, \
        it will return an Exception"""
        )
    def get_actor(info: type_info, name: str, actor_id: Optional[str] = None) -> actor_type_base:
        with session_local() as session:
            if actor_id is not None:
                actor = session.query(actor_model).where(and_(actor_model.name == name, actor_model.uuid == actor_id)).first()

                if not actor:
                    raise Exception(f"Actor '{name}' or ID '{actor_id}' not found")
            else:
                actor = session.query(actor_model).filter(actor_model.name == name).first()

                if not actor:
                    raise Exception(f"Actor '{name}' not found")
            
            return actor_type_base(
                uuid=actor.uuid,
                name=actor.name,
                birth_date=actor.birth_date,
                biography=actor.biography,
                nationality=actor.nationality,
                timestamp=actor.timestamp
            )
    
    @strawberry.field(
        description="""Returns data from the FilmActors pivot table. \
        This can be used if you want ID data from each Film or Actor table."""
        )
    def get_film_actors(skip: int = 0, limit: int = 100) -> list[film_actor_type_base]:
        with session_local() as session:
            film_actors = session.query(film_actor_model).offset(skip).limit(limit).all()

            if not film_actors:
                raise Exception("FilmActors table does not have any data or is empty")

            return [film_actor_type_base(
                uuid=film_actor.uuid,
                film_id=film_actor.film_id,
                actor_id=film_actor.actor_id,
                timestamp=film_actor.timestamp
            ) for film_actor in film_actors]
    
    @strawberry.field(
        description="""Returns data from the Films table combine with Actor table. \
        This can be used if you want ID data from Films table and Actors table in it."""
        )
    def get_one_film_combine_actors(info: type_info, title: str) -> film_type:
        with session_local() as session:
            data_combine = session.query(film_model).options(joinedload(film_model.actors)).where(film_model.title == title).first()

            actor_data = []
            for d in data_combine.actors:
                actor = actor_type_base(
                    uuid=d.uuid,
                    name=d.name,
                    birth_date=d.birth_date,
                    biography=d.biography,
                    nationality=d.nationality,
                    timestamp=d.timestamp
                    )
                actor_data.append(actor)
            
            return film_type(
                uuid=data_combine.uuid,
                title=data_combine.title,
                genre=data_combine.genre,
                language=data_combine.language,
                release=data_combine.release,
                is_premiere=data_combine.is_premiere,
                timestamp=data_combine.timestamp,
                actors=actor_data
            )
    
    @strawberry.field(
        description="""Returns data from the Actors table. \
        This can be used if you want ID data from each Film or Actor table."""
        )
    def get_one_actor_combine_films(info: type_info, name: str) -> actor_type:
        with session_local() as session:
            data_combine = session.query(actor_model).options(joinedload(actor_model.films)).where(actor_model.name == name).first()

            film_data = []
            for d in data_combine.films:
                film = film_type_base(
                    uuid=d.uuid,
                    title=d.title,
                    genre=d.genre,
                    language=d.language,
                    release=d.release,
                    is_premiere=d.is_premiere,
                    timestamp=d.timestamp
                    )
                film_data.append(film)
            
            return actor_type(
                uuid=data_combine.uuid,
                name=data_combine.name,
                birth_date=data_combine.birth_date,
                biography=data_combine.biography,
                nationality=data_combine.nationality,
                timestamp=data_combine.timestamp,
                films=film_data
            )
    



        
