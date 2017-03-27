from flask import Flask, Response, jsonify, render_template, request, redirect
app = Flask(__name__)

import time
from time import sleep

from lxml import html
import requests

emails_addresses = []

@app.route('/')
def hello_world():
	author = "Me"
	name = "You"

	if request.headers.get('accept') == 'text/event-stream':
		messages = []
		def script():

			page = requests.get('http://menus.tufts.edu/foodpro/shortmenu.asp?sName=TUFTS' +
					'+DINING&locationNum=11&locationName=Dewick-MacPhie' + 
					'+Dining+Center&naFlag=1&WeeksMenus=This+Week%27s+Menus' +
					'&myaction=read&dtdate=3%2F31%2F2017')

			#a lot of code goes here
			yield page

			#more code
			sleep(10)
			yield "data: Part B completed.\n\n"

			#more code
			sleep(10)
			yield "data: Part C completed.\n\n"

		return Response(script(), content_type='text/event-stream')

	return render_template('index.html', author=author, name=name)


@app.route('/signup', methods = ['POST'])
def signup():
	email = request.form['email']
	emails_addresses.append(email)
	print(emails_addresses)



	return redirect('/')




if __name__ == "__main__":
    app.run() 