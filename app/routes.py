
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import ApiKeyInputForm
from werkzeug.urls import url_parse
import requests 
import random

#home page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title="Home Page")

#about page
@app.route('/about')
def about():
	return render_template('about.html', title="About")

#request page
@app.route('/nasarequest', methods=['GET', 'POST'])
def nasarequest():
	#form to input api key
	form = ApiKeyInputForm()
	if form.validate_on_submit():
		apikey = form.apikey.data #set apikey to input
		#check which API to request
		if form.apod.data:
			url = 'https://api.nasa.gov/planetary/apod?' #set API url
			page = 'nasaApod.html' #set redirect template
		elif form.rover.data:
			sol = random.randint(1,2500) #random number for sol
			url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&page=2&' #set API url with random sol input
			page = 'nasaRover.html' #set redirect template
		res = requests.get(f'{url}api_key={apikey}') #call api
		status = res.status_code #get api page status to validate apikey
		if status == 403: #invalid api key error
			flash('Please enter a valid API Key or use the DEMO_KEY')
			return redirect(url_for('nasarequest'))
		elif status == 429: #too many requests error
			flash('Too many requests, please enter a different API Key or try again later')
			return redirect(url_for('nasarequest'))
		apijson = res.json() #store json from api
		return render_template(page, apidata=apijson) #redirect to api display page
	return render_template('nasarequest.html', form=form)
#(my nasa apikey - lou5l9csSbcNzkWzpwMBdGCuDtWEmXPiCk5ZhReO)

#apod display page
@app.route('/nasaApod')
def nasaApod():
	return render_template('nasaApod.html', apidata=apijson)

#rover display page
@app.route('/nasaRover')
def nasaRover():
	return render_template('nasaRover.html', apidata=apijson)
