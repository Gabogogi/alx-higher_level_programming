#!/usr/bin/python3
"""Lists all State objects and corresponding City objects"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Query to get all State and City objects
    results = session.query(State).order_by(State.id).all()

    for state in results:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
