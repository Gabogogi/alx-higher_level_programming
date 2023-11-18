#!/usr/bin/python3
"""
delete all State objects with 'a' in 
name containing the letter 'a' the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: <username> <password> <databaseName>")
        exit(1)

    username, password, db_name = argv[1], argv[2], argv[3]

    #connection to database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.bind = engine

    #creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #queries
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    
    for state in states_to_delete:
        session.delete(state)
    
    session.commit()

   
    session.close()