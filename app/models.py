# app/models.py

import strawberry

from app.config import Base as base
from sqlalchemy.orm import relationship
from strawberry.fastapi import GraphQLRouter
from sqlalchemy import (
    Column, 
    DateTime, 
    String, 
    Integer,
    Boolean,
    Date,
    Text,
    ForeignKey
    )
from datetime import datetime, date


class FilmActor(base):
    __tablename__ = "filmactors"

    uuid = Column(String(36), primary_key=True, nullable=False)
    film_id = Column("film_id", ForeignKey("films.uuid"), nullable=False)
    actor_id = Column("actor_id", ForeignKey("actors.uuid"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow())

class Film(base):
    __tablename__ = "films"

    uuid = Column(String(36), primary_key=True, nullable=False)
    title = Column(String(255), nullable=False, unique=True)
    genre = Column(String(255), nullable=False)
    language = Column(String(255), nullable=False)
    release = Column(Date, nullable=True, default=date(year=2011, month=1, day=1))
    is_premiere = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow())

    # create actors relationship
    actors = relationship("Actor", secondary="filmactors", back_populates="films")

class Actor(base):
    __tablename__ = "actors"

    uuid = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=True, default=date.today())
    biography = Column(Text, nullable=True)
    nationality = Column(String(255), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow())

    films = relationship("Film", secondary="filmactors", back_populates="actors")

