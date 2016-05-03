"""
    flaskbb.exceptions
    ~~~~~~~~~~~~~~~~~~

    Exceptions implemented by FlaskBB.

    :copyright: (c) 2015 by the FlaskBBB Team.
    :license: BSD, see LICENSE for more details
"""
from werkzeug.exceptions import HTTPException, Forbidden


class FlaskBBError(HTTPException):
    "Root exception for FlaskBB"
    description = "An internal error has occured"


class AuthorizationRequired(FlaskBBError, Forbidden):
    description = "Authorization is required to access this area."


class AuthenticationError(FlaskBBError):
    description = "Invalid username and password combination."


class LoginAttemptsExceeded(FlaskBBError):
    description = "The user has entered the wrong password too many times."

    def __init__(self, user):
        super(LoginAttemptsExceeded, self).__init__()
        self.user = user
