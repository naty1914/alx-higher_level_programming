#!/usr/bin/python3
"""
A Module  that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    sts = sess.query(State).outerjoin(City).order_by(State.id, City.id).all()
    for st in sts:
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("    {}: {}".format(ct.id, ct.name))
