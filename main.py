# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from trfa import app_api1
from bp_projects.projects import app_projects # Blueprint directory import projects definition

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_api1)
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/team/')  # connects /stub/ URL to stub() function
def team():
    return render_template("team.html")

@app.route('/AgileMethodologyDiagram/')  # connects /stub/ URL to stub() function
def amd():
    return render_template("amd.html")

@app.route('/Pong/')  # connects /stub/ URL to stub() function
def pong():
    return render_template("pong.html")

@app.route('/Blackjack/')  # connects /stub/ URL to stub() function
def blackjack():
    return render_template("games/blackjack.html")

@app.route('/GroupProjectPlan/')  # connects /stub/ URL to stub() function
def plan():
    return render_template("plan.html")

# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
