from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseTeamSetup import *

engine = create_engine('sqlite:///fantasySoccerTeam.db')

Base.metadata_bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# juventus = Team(name="Juventus", year_founded=1981)

# ronaldo = Player(name="C Ronaldo", position="striker", age=33, team=juventus )



barcelona = Team(name="Barcelona", year_founded=1977)

messi = Player(name="Messi", position="striker", age=32, team=barcelona )

session.add(barcelona)
session.add(messi)
session.commit()