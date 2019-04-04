"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Website import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/')
@app.route('/about')
def about():
    """Renders the home page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message=''
    )

@app.route('/')
@app.route('/photogallery')
def photogallery():
    """Renders the Photo Gallery page."""
    return render_template(
        'photogallery.html',
        title='Photo Gallery',
        year=datetime.now().year,
        message=''
    )

@app.route('/')
@app.route('/dailyposts')
def dailyposts():
    """Renders the Photo Gallery page."""
    return render_template(
        'dailyposts.html',
        title='Daily Posts',
        year=datetime.now().year,
        month=datetime.now().month,
        day=datetime.now().day,
        message=''
    )

@app.route('/')
@app.route('/downloads')
def downloads():
    """Renders the Photo Gallery page."""
    return render_template(
        'downloads.html',
        title='Downloads',
        year=datetime.now().year,
        message='Downloads'
    )



