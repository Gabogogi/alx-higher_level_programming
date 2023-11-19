#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <username> <password> <databaseName>".format(argv[0]))
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    # Creating the connection to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Creating the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all City objects with the associated State object
    cities = (
        session.query(City)
        .join(State)
        .order_by(City.id)
        .all()
    )

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
