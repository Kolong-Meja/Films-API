# app/main.py

"""Main program of this project."""

import strawberry
import uvicorn
import os

from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
from app.query import Query as app_query
from app.mutation import Mutation as app_mutation
from app.database.sql_tool import query
from app.database.query import (
    create_films_table_query, 
    create_actors_table_query,
    create_film_actors_table_query
    )
from app.config import (
    APP_DEV_HOST, 
    APP_DEV_PORT
    )


# define requirement for graphql
graphql_schema = strawberry.Schema(
    query=app_query, 
    mutation=app_mutation
    )
graphql_router = GraphQLRouter(
    schema=graphql_schema, 
    debug=True, 
    graphiql=True
    )
    
# define the app.
app = FastAPI()
app.include_router(router=graphql_router, prefix="/graphql")

# run the program.
if __name__ == "__main__":
    uvicorn.run("__main__:app", host=APP_DEV_HOST, port=APP_DEV_PORT, use_colors=True, reload=True)
    