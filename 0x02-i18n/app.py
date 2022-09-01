#!/usr/bin/env python3
"""
Script that starts a basic flask Babel setup
"""
from datetime import timezone
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Union, Optional
from pytz import timezone
import pytz.exceptions

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """GET /
    Return: The render of index.html"""
    return render_template('index.html')


class Config(object):
    """flask app config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Set the above class object as the configuration for the app
app.config.from_object('app.Config')


@babel.localeselector
def get_locale():
    """Determines the best match for supported languages"""
    # Checks if there is a locale parameter/query string
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    # Check if there is a locale in an existing user's profile
    elif g.user and g.user.get('locale')\
            and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    # Return for default
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ Returns user dict if ID can be found """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """ Finds user and sets as global on flask.g.user """
    g.user = get_user()
    g.current_time = format_datetime(datetime.now())


@babel.timezoneselector
def get_timezone() -> Optional[str]:
    """ Determines the appropriate user timezone. """
    user_timezone = request.args.get('timezone', None)
    if user_timezone:
        try:
            return timezone(user_timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'
    if g.user:
        try:
            return timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'
    default_timezone = app.config['BABEL_DEFAULT_TIMEZONE']
    return request.accept_languages.best_match([default_timezone])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
