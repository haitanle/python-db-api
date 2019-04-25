from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseTeamSetup import Base, Team, Player

app = Flask(__name__)

#add sqlalchemy CRUD
engine = create_engine('sqlite:///fantasySoccerTeam.db')
Base.metadata_bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def show_teams():

	teams = session.query(Team).all()
	output = "<h1>Champions League!</h1><p>Go to url: /team/{id}/ to see your team:</p>"
	for team in teams: 
		output+=("(id: %s) %s %s <br>"%(team.id, team.name, team.year_founded))
	return output

@app.route('/team/<int:team_id>/')
def team_roster(team_id):
	team = session.query(Team).filter_by(id=team_id).one()
	players = session.query(Player).filter_by(team_id=team_id).all()
	return render_template('team.html', team=team, players=players)

if __name__ == '__main__':
	print('startin server...')
	app.debug = True
	app.run(host='0.0.0.0', port=8000)