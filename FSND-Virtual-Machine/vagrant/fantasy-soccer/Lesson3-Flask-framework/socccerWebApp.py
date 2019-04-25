from flask import Flask, render_template, url_for, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseTeamSetup import Base, Team, Player
import cgi

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

@app.route('/team/<int:team_id>/', methods=['GET'])
def team_roster(team_id):
	team = session.query(Team).filter_by(id=team_id).one()
	players = session.query(Player).filter_by(team_id=team_id).all()
	return render_template('team.html', team=team, players=players)

@app.route('/<int:team_id>/add_player', methods=['POST'])
def add_player_to(team_id):
	if request.method == 'POST':
		print('adding player...')

		playerName = request.form['name']
		playerPosition = request.form['position']
		playerAge = request.form['age']

		newPlayer = Player(team_id=team_id, name=playerName, position = playerPosition, age=playerAge)
		session.add(newPlayer)
		session.commit()

		return redirect(url_for('team_roster',team_id=team_id), code=303)

if __name__ == '__main__':
	print('startin server...')
	app.debug = True
	app.run(host='0.0.0.0', port=8000)