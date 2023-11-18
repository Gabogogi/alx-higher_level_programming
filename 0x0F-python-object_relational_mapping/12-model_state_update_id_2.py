#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()


    state_to_update = session.query(State).filter_by(id=2).first()
    state_to_update.name = "New Mexico"
    session.commit()

   
    session.close()