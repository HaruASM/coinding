"""
Routes and views for the flask application.
"""

from __future__ import with_statement
from contextlib import closing
from datetime import datetime
from flask import render_template
from flask import request
from flask import jsonify
from HelloFlask import *

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    
    trading.RunSimulation()
    if request.method == 'POST':
        print("POST message received")
        return jsonify(data="1807" , code=5)

    else:
        """Renders the home page."""
        return render_template(
            'index.html',
            title='Home Page',
            year=datetime.now().year        
        )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
