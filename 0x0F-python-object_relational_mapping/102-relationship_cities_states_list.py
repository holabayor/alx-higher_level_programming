#!/usr/bin/python3
"""
    Script that lists all City objects
    from the database hbtn_0e_101_usa
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
