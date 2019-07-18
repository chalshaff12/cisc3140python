
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import ApiKeyInputForm
from werkzeug.urls import url_parse
import requests 

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
	form = ApiKeyInputForm()
	if form.validate_on_submit():
		apikey = form.apikey.data #set apikey to input
		res = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={ apikey }') 
		status = res.status_code
		if status == 403:
			flash('Please enter a valid API Key or use the DEMO_KEY')
			return redirect(url_for('nasarequest'))
		apijson = res.json()
		return render_template('nasaApod.html', apidata=apijson)
	return render_template('nasarequest.html', form=form)
#(my nasa apikey - lou5l9csSbcNzkWzpwMBdGCuDtWEmXPiCk5ZhReO)

@app.route('/nasaApod')
def nasaApod():
	return render_template('nasaApod.html', apidata=apijson)


