from flask import Flask, render_template, url_for, request, redirect, flash
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
	return render_template('main.html', teams=teams)

@app.route('/team/<int:team_id>/', methods=['GET'])
def team_roster(team_id):
	team = session.query(Team).filter_by(id=team_id).one()
	players = session.query(Player).filter_by(team_id=team_id).all()
	return render_template('team.html', team=team, players=players)

@app.route('/<string:team_id>/add_player', methods=['GET','POST'])
def add_player_to(team_id):
	if request.method == 'GET':
		team = session.query(Team).filter_by(id=team_id).one()
		return render_template('add_player.html', team=team)

	if request.method == 'POST':
		print('adding player...')

		playerName = request.form['name']
		playerPosition = request.form['position']
		playerAge = request.form['age']

		newPlayer = Player(team_id=team_id, name=playerName, position = playerPosition, age=playerAge)
		session.add(newPlayer)
		session.commit()
		flash('Goal! New player added! %s'%(playerName))

		return redirect(url_for('team_roster',team_id=team_id), code=303)

if __name__ == '__main__':
	app.secret_key = 'secretsecret'
	print('startin server...')
	app.debug = True
	app.run(host='0.0.0.0', port=8000)