from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseTeamSetup import *

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
				print team.name 
				teams_display+=(team.name+'<br />')
				teams_display+=('<a href="/%s/edit">Edit</a><br /><a href="#">Delete</a><br />'%team.id)

			output+=teams_display
			output+="</body></html>"
			self.wfile.write(output)
		elif self.path.endswith("/edit"):
			self.send_response(200)
			self.send_header('Content-type','text/html; charset=utf-8')
			self.end_headers()

			teamID = self.path.split("/")[1]
			team = session.query(Team).filter_by(id=teamID).one()
			output = "teamID:%s  teamName:%s  year:%s"%(team.id, team.name, team.year_founded)
			self.wfile.write(output)


if __name__== '__main__':
	server_address = ('', 8000)
	server = HTTPServer(server_address, Handler_class)
	server.serve_forever()