"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ExampleWidget import app

@app.route('/')
@app.route('/red')
def red():
    """Renders the red page."""
    return render_template(
        'red.html',
        title='red page',
    )

@app.route('/green')
def green():
    """Renders the green page."""
    return render_template(
        'green.html',
        title='green page',
    )

@app.route('/blue')
def blue():
    """Renders the blue page."""
    return render_template(
        'blue.html',
        title='blue page',
    )

@app.route('/yellow')
def yellow():
    """Renders the yellow page."""
    return render_template(
        'yellow.html',
        title='yellow page',
    )

@app.route('/orange')
def orange():
    """Renders the orange page."""
    return render_template(
        'orange.html',
        title='orange page',
    )

@app.route('/brown')
def brown():
    """Renders the brown page."""
    return render_template(
        'brown.html',
        title='brown page',
    )

@app.route('/pink')
def pink():
    """Renders the pink page."""
    return render_template(
        'pink.html',
        title='pink page',
    )

@app.route('/purple')
def purple():
    """Renders the purple page."""
    return render_template(
        'purple.html',
        title='purple page',
    )

@app.route('/turquoise')
def turquoise():
    """Renders the turquoise page."""
    return render_template(
        'turquoise.html',
        title='turquoise page',
    )

@app.route('/white')
def white():
    """Renders the white page."""
    return render_template(
        'white.html',
        title='white page',
    )

@app.route('/black')
def black():
    """Renders the black page."""
    return render_template(
        'black.html',
        title='black page',
    )

@app.route('/grey')
def grey():
    """Renders the grey page."""
    return render_template(
        'grey.html',
        title='grey page',
    )