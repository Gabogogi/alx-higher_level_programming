#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <username> <password> <databaseName>")
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    # Creating the connection to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Creating the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating the State "California" with the City "San Francisco"
    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)
    session.commit()

    # Closing the session
    session.close()