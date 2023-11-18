#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: <username> <password> <databaseName>")
        exit(1)

    username, password, db_name, state_name = argv[1], argv[2], argv[3], argv[4]

    
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()


    state_to_search = session.query(State).filter_by(name=state_name).first()

    # Displaying the result
    if state_to_search:
        print(state_to_search.id)
    else:
        print("Not found")

    # Closing the session
    session.close()