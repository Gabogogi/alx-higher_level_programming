#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State


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

    # Querying for the first State object
    all_city = session.query(City, State).join(State).order_by(City.id).all()
    
    for city, state in all_city:
        print(f"{state.name}: ({city.id}) {city.name}")


    # Closing the session
    session.close()