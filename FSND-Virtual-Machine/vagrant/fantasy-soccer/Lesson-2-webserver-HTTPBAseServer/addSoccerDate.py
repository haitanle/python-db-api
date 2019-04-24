from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseTeamSetup import *

engine = create_engine('sqlite:///fantasySoccerTeam.db')

Base.metadata_bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#CREATE


# juventus = Team(name="Juventus", year_founded=1981)

# ronaldo = Player(name="C Ronaldo", position="striker", age=33, team=juventus )



# barcelona = Team(name="Barcelona", year_founded=1977)

# session.add(Player(name="Busquet", position="mid-fielder", age=30, team=barcelona ))
# session.add(Player(name="Iniesta", position="mid-fielder", age=35, team=barcelona ))

# session.add(Player(name="Henry", position="striker", age=40, team=barcelona ))

# session.add(Player(name="Puyol", position="defender", age=32, team=barcelona ))
# session.add(Player(name="Pique", position="defender", age=32, team=barcelona ))

# session.add(Player(name="Xavi", position="mid-fielder", age=32, team=barcelona ))

# session.commit()



# juventus = Team(name="Barcelona", year_founded=1977)

# session.add(Player(name="Dybala", position="mid-fielder", age=30, team=juventus ))
# session.add(Player(name="Khediera", position="mid-fielder", age=35, team=juventus ))

# session.add(Player(name="Manduzic", position="striker", age=40, team=juventus ))

# session.add(Player(name="Bonacci", position="defender", age=32, team=juventus ))
# session.add(Player(name="Chielenni", position="defender", age=32, team=juventus ))

# session.add(Player(name="D Costa", position="mid-fielder", age=32, team=juventus ))

# session.commit()


city = Team(name="Manchester City", year_founded=1988)

session.add(city)

session.add(Player(name="Aquero", position="striker", age=33, team=city ))
session.add(Player(name="De Buyne", position="mid-fielder", age=30, team=city ))
session.add(Player(name="Silva", position="mid-fielder", age=35, team=city ))
session.add(Player(name="Jesus", position="striker", age=40, team=city ))
session.add(Player(name="Stones", position="defender", age=32, team=city ))
session.add(Player(name="Laporte", position="defender", age=32, team=city ))
session.add(Player(name="Sterling", position="mid-fielder", age=32, team=city ))

session.commit()




#READ 

# teams = session.query(Team).first()
# print teams.name


# players = session.query(Player).all()
# for player in players:
# 	print player.name


#UPDATE'

# players = session.query(Player).filter_by(team_id = 4).all()

# for player in players:
# 	player.team_id = 5
# 	session.add(player)

# session.commit()





#DELETE

# item_to_delete = session.query(Player).filter_by(id="1").one()

# session.delete(item_to_delete)
# session.commit()