# app/mutation.py

import strawberry

from uuid import uuid4 as uuid
from strawberry.types import Info as type_info
from app.inputs import (
    FilmCreateInput as film_create_input,
    FilmUpdateInput as film_update_input,
    ActorCreateInput as actor_create_input,
    ActorUpdateInput as actor_update_input,
    FilmActorInput as film_actor_input,
    )
from app.models import (
    Film as film_model,
    Actor as actor_model,
    FilmActor as film_actor_model,
    )
from app.types import (
    Response as message_response,
    FilmCreateResponse as film_create_response,
    FilmUpdateResponse as film_update_response,
    ActorCreateResponse as actor_create_response,
    ActorUpdateResponse as actor_update_response,
    FilmActorResponse as film_actor_response,
    FilmTypeBase as film_type_base,
    ActorTypeBase as actor_type_base,
    FilmUpdateType as film_update_type,
    ActorUpdateType as actor_update_type,
    FilmActorTypeBase as film_actor_type_base,
    )
from app.config import SessionLocal as session_local


"""
TODO: Define main Mutation class BELOW!
"""
# define our Mutation class
@strawberry.type(
    description="""Is a command to modify data from the server. \
    These commands are similar to the POST, PUT, FETCH, and DELETE methods of the Restful API. \
    however, it's just written in GraphQL format"""
    )
class Mutation:
    @strawberry.mutation(
        description="""Useful for creating one Film data.\n\
        NOTE: there is some Optional data such as UUID and timestamp. \
        You can leave these optional fields blank, \
        or also fill in these fields with your own data"""
        )
    # create film data.
    def add_film(
        self, 
        info: type_info,
        input: film_create_input,
        ) -> film_create_response:
        with session_local() as session:
            database_film = film_model(
                uuid=uuid().hex,
                title=input.title,
                genre=input.genre,
                language=input.language,
                release=input.release,
                is_premiere=input.is_premiere,
                timestamp=input.timestamp
            )

            session.add(database_film)
            session.commit()
            session.refresh(database_film)

        new_film = film_type_base(
            uuid=database_film.uuid,
            title=database_film.title,
            genre=database_film.genre,
            language=database_film.language,
            release=database_film.release,
            is_premiere=database_film.is_premiere,
            timestamp=database_film.timestamp,
        )
        response = message_response(message=f"Film '{input.title}' successfully created.")
        
        return film_create_response(film=new_film, response=response)
    
    @strawberry.mutation(
        description="""Useful for updating one Film data.\n\
        NOTE: All field are Optional You can leave these optional fields blank, \
        or also fill in these fields with your own data"""
        )
    def update_film(
        self,
        info: type_info,
        title: str,
        data: film_update_input
    ) -> film_update_response:
        with session_local() as session:
            film = session.query(film_model).filter(film_model.title == title).first()

            if not film:
                raise Exception(f"Film '{title}' not found.")
            
            for key, value in data.__dict__.items():
                setattr(film, key, value)
            
            session.commit()
            session.refresh(film)
        
        update_film = film_update_type(
            title=film.title,
            genre=film.genre,
            language=film.language,
            release=film.release,
            is_premiere=film.is_premiere,
            timestamp=film.timestamp
        )
        response = message_response(message=f"Film '{title}' successfully updated.")

        return film_update_response(film=update_film, response=response)
    
    @strawberry.mutation(
        description="""Useful for deleting one Film data.\n\
        NOTE: All field are Optional You can leave these optional fields blank, \
        or also fill in these fields with your own data"""
        )
    def delete_film(
        self,
        info: type_info,
        title: str,
    ) -> message_response:
        with session_local() as session:
            film = session.query(film_model).filter(film_model.title == str).first()

            if not film:
                raise Exception(f"Film '{title}' not found.")
            
            session.delete(film)
            session.commit()
            session.close()
        
        return message_response(
            message=f"Film {title} successfully deleted."
        )
    
    @strawberry.mutation(
        description="""Useful for creating one Actor data.\n\
        NOTE: there is some Optional data such as UUID and timestamp. \
        You can leave these optional fields blank, \
        or also fill in these fields with your own data"""
        )
    def add_actor(
        self, 
        info: type_info,
        input: actor_create_input
        ) -> actor_create_response:
            with session_local() as session:
                database_actor = actor_model(
                    uuid=uuid().hex,
                    name=input.name,
                    birth_date=input.birth_date,
                    biography=input.biography,
                    nationality=input.nationality,
                    timestamp=input.timestamp
                )

                session.add(database_actor)
                session.commit()
                session.refresh(database_actor)
            
            new_actor = actor_type_base(
                uuid=database_actor.uuid,
                name=database_actor.name,
                birth_date=database_actor.birth_date,
                biography=database_actor.biography,
                nationality=database_actor.nationality,
                timestamp=database_actor.timestamp
            )

            response = message_response(message=f"Actor '{input.name}' successfully created.")

            return actor_create_response(
                actor=new_actor,
                response=response
            )
    
    @strawberry.mutation(
        description="""Useful for updating one Actor data.\n\
        NOTE: All field are Optional You can leave these optional fields blank, \
        or also fill in these fields with your own data"""
        )
    def update_actor(
        self, 
        info: type_info, 
        name: str, 
        data: actor_update_input
        ) -> actor_update_response:
            with session_local() as session:
                actor = session.query(actor_model).filter(actor_model.name == name).first()

                if not actor:
                    raise Exception(f"Actor '{name}' not found.")
                
                for key, value in data.__dict__.items():
                    setattr(actor, key, value)

                session.commit()
                session.refresh(actor)

            update_actor = actor_update_type(
                name=actor.name,
                birth_date=actor.birth_date,
                biography=actor.biography,
                nationality=actor.nationality,
                timestamp=actor.timestamp
            )

            response = message_response(message=f"Actor '{name}' successfully updated.")

            return actor_update_response(
                actor=update_actor,
                response=response
            )
    
    @strawberry.mutation(
        description="""Useful for deleting one Actor data.\n\
        NOTE: All field are Optional You can leave these optional fields blank, \
        or also fill in these fields with your own data"""
        )
    def delete_actor(
        self, 
        info: type_info, 
        name: str
        ) -> message_response:
            with session_local() as session:
                actor = session.query(actor_model).filter(actor_model.name == name).first()

                if not actor:
                    raise Exception(f"Actor '{name}' not found.")
                
                session.delete(actor)
                session.commit()
                session.close()
            
            return message_response(
                message=f"Actor {name} successfully deleted."
            )
    
    @strawberry.mutation(
        description="""This is useful for creating a relationship between\
        the Film table and the Actor table."""
        )
    def create_film_actor_connection(
        self, 
        info: type_info, 
        data: film_actor_input
        ) -> film_actor_response:
            with session_local() as session:
                film = session.query(film_model).filter(film_model.uuid == data.film_id).first()
                actor = session.query(actor_model).filter(actor_model.uuid == data.actor_id).first()

                if not film:
                    raise Exception(f"Film with ID '{data.film_id}' not found.")
                
                if not actor:
                    raise Exception(f"Actor with ID '{data.actor_id}' not found.")
                
                film_actor = film_actor_model(
                    uuid=uuid().hex,
                    film_id=film.uuid,
                    actor_id=actor.uuid,
                    timestamp=data.timestamp
                )

                session.add(film_actor)
                session.commit()
                session.refresh(film_actor)
            
            new_film_actor = film_actor_type_base(
                uuid=film_actor.uuid,
                film_id=film_actor.film_id,
                actor_id=film_actor.actor_id,
                timestamp=film_actor.timestamp
            )

            response = message_response(message=f"Films and Actors successfully connected.")

            return film_actor_response(
                film_actor=new_film_actor,
                response=response
            )
    
    @strawberry.field(
        description="""This is useful for deleting the relationship\
        between the Film table and the Actor table.\nNOTE: you must input UUID from FilmActors \
        table as an argument for deleting the connection between Film and Actor table"""
        )
    def delete_film_actor_connection(
        self, 
        info: type_info, 
        film_actors_id: str
        ) -> message_response:
            with session_local() as session:
                film_actor = session.query(film_actor_model).filter(film_actor_model.uuid == film_actors_id).first()

                if not film_actor:
                    raise Exception(f"Film with ID '{data.film_id}' or Actor with ID '{data.actor_id}' not found.")
                
                session.delete(film_actor)
                session.commit()
                session.close()

            return message_response(
                message=f"Film Actor with Film ID '{film_actor.film_id}' and Actor ID '{film_actor.actor_id}' successfully deleted."
            )
