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
			self.send_header('Content-type','text/plain; charset=utf-8')
			self.end_headers()

			teams = session.query(Team).all()
			output = ''
			for team in teams: 
				print team.name 
				output+=(team.name+'\n') # or output as HTML
			self.wfile.write(output)

if __name__== '__main__':
	server_address = ('', 8000)
	server = HTTPServer(server_address, Handler_class)
	server.serve_forever()