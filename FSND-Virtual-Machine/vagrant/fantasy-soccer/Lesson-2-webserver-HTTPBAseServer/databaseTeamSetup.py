import sys
import os

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Team(Base):
	__tablename__ = 'team'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable=False)
	year_founded = Column(Integer, nullable=False)

class Player(Base):
	__tablename__ = 'player'

	team_id = Column(Integer, ForeignKey('team.id'))
	team = relationship(Team)
	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	position = Column(String(50), nullable=False)
	age = Column(Integer)

	@property
	def tan(self):
		return {
			'name': self.name,
			'id': self.id,
			'position': self.position,
			'age': self.age
		}
	

#end of file
engine = create_engine('sqlite:///fantasySoccerTeam.db')
Base.metadata.create_all(engine)