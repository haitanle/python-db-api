from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseTeamSetup import *

import cgi

engine = create_engine('sqlite:///fantasySoccerTeam.db')
Base.metadata_bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Handler_class(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.endswith("/"):
			self.send_response(200)
			self.send_header('Content-type','text/html; charset=utf-8')
			self.end_headers()

			teams = session.query(Team).all()
			output = "<html><body><h1>Champions League!</h1>"
			teams_display = ''
			for team in teams: 
				teams_display+=("%s %s %s <br>"%(team.id, team.name, team.year_founded))
				teams_display+=('<a href="/%s/edit">Edit</a><br /><a href="#">Delete</a><br />'%team.id)

			output+=teams_display

			form = "<br><br><h2>Add new team</h2><form action='/add_team' method='post' enctype='multipart/form-data'> \
					Name:\
					<input type='text' name='name' ><br> \
					year founded: \
					<input type='number' name='year_founded'><br> \
					<br><br> \
					<input type='submit' value='Create'> \
					<button type='reset' value='Reset'>Reset</button> \
					</form>"

			output+=form

			output+="</body></html>"
			self.wfile.write(output)
		elif self.path.endswith("/edit"):
			self.send_response(200)
			self.send_header('Content-type','text/html; charset=utf-8')
			self.end_headers()

			teamID = self.path.split("/")[1]
			team = session.query(Team).filter_by(id=teamID).one()
			#output = "teamID:%s  teamName:%s  year:%s"%(team.id, team.name, team.year_founded)

			output ="<html><body><h1>Update</h1><form action='/%s/edit_done' method='post' enctype='multipart/form-data'> \
					Id: \
					<input type='number' name='id' value=%s disabled><br> \
					Name:\
					<input type='text' name='name' value=%s><br> \
					year founded: \
					<input type='number' name='year_founded' value=%s><br> \
					<br><br> \
					<input type='submit' value='Edit'> \
					<a href='/'>Cancel</a> \
					</form></body></html>"%(team.id, team.id, team.name, team.year_founded)

			self.wfile.write(output)
		else:
			self.send_error(404, 'File Not Found: %s' % self.path)

	def do_POST(self):
		ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
		if ctype == 'multipart/form-data' and self.path.endswith("edit_done"):
			fields = cgi.parse_multipart(self.rfile, pdict)

			teamId = self.path.split("/")[1]
			newName = fields.get('name')[0]
			newYear = fields.get('year_founded')[0]

			team = session.query(Team).filter_by(id=teamId).one()
			team.name = newName
			team.year_founded = newYear

			session.add(team)
			session.commit()

			self.send_response(303)
			self.send_header('Location','/')
			self.end_headers()

		if ctype == 'multipart/form-data' and self.path.endswith("add_team"):
			fields = cgi.parse_multipart(self.rfile, pdict)

			newName = fields.get('name')[0]
			newYear = fields.get('year_founded')[0]

			team = Team(name=newName, year_founded=newYear)
			session.add(team)
			session.commit()

			self.send_response(303)
			self.send_header('Location','/')
			self.end_headers()


if __name__== '__main__':
	server_address = ('', 8000)
	server = HTTPServer(server_address, Handler_class)
	server.serve_forever()