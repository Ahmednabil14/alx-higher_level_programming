#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]
    ))
    session = sessionmaker(bind=engine)
    Session = session()
    states = Session.query(State)
    if (states.count() == 0):
        print("Nothing")
    for state in states:
        if (state.id == 1):
            print("{}: {}".format(state.id, state.name))
            break
