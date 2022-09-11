from . import main
from flask import session

@main.route("/")
def greet():
    return "Hello Kusu and session name is {0}".format(session.get("name"))