from flask import Flask 
app = Flask(__name__)

@app.route('/')
def soccer_time():
	return 'Hello Soccer!'

if __name__ == '__main__':
	print('startin server...')
	app.debug = True
	app.run(host='0.0.0.0', port=8000)