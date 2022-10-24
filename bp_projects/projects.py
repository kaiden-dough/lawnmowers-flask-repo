from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/KaidenTheKangaroo/')
def kaiden():
    return render_template("kaiden.html")

@app_projects.route('/theo/')
def theo():
    return render_template("theo.html")

@app_projects.route('/Mani the Mandrill/')
def mani():
    return render_template("mani.html")

@app_projects.route('/kush/')
def kush():
    return render_template("kush.html")

@app_projects.route('/AgileMethodologyDiagram/')
def amd():
    return render_template("amd.html")

@app_projects.route('/GroupProjectPlan/')
def plan():
    return render_template("plan.html")

@app_projects.route('/JokeboxGame/')
def jokebox():
    return render_template("jokebox.html")