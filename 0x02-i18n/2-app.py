#!/usr/bin/env python3
"""
Script that starts a basic flask Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """GET /
    Return: The render of 2-index.html"""
    return render_template('2-index.html')


class Config(object):
    """flask app config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Set the above class object as the configuration for the app
app.config.from_object('2-app.Config')


@babel.localeselector
def get_locale():
    """Determines the best match for supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
