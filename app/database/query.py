# CREATE STATEMENT AREA!
create_films_table_query = """
CREATE TABLE IF NOT EXISTS Films (
    uuid VARCHAR(36) NOT NULL,
    title VARCHAR(255) NOT NULL UNIQUE,
    genre VARCHAR(255) NOT NULL,
    language VARCHAR(255) NOT NULL,
    release DATE NULL DEFAULT CURRENT_DATE,
    is_premiere BOOLEAN DEFAULT FALSE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (uuid)
)
"""

create_actors_table_query = """
CREATE TABLE IF NOT EXISTS Actors (
    uuid VARCHAR(36) NOT NULL,
    name VARCHAR(255) NOT NULL,
    birth_date DATE NULL DEFAULT CURRENT_DATE,
    biography TEXT NULL,
    nationality VARCHAR(255) NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (uuid)
)
"""

create_film_actors_table_query = """
CREATE TABLE IF NOT EXISTS FilmActors (
    uuid VARCHAR(36) NOT NULL,
    film_id VARCHAR(36) NOT NULL,
    actor_id VARCHAR(36) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (uuid),
    CONSTRAINT fk_film_actors FOREIGN KEY (film_id) REFERENCES films(uuid) ON DELETE CASCADE,
    CONSTRAINT fk_actor_films FOREIGN KEY (actor_id) REFERENCES actors(uuid) ON DELETE CASCADE
)
"""



