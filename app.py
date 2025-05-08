from pathlib import Path
import sys
import os
import subprocess
import shutil

DIR_ROOT = Path(__file__).resolve().parents[0]
from src import *

from flask import Flask, request, render_template, redirect, jsonify
import json
import yaml

###### Setup #####

app = Flask(__name__, static_url_path='/s/', static_folder='static')

####################

def render_page(template, data):
    return render_template(template, data=data)

@app.route("/")
@app.route("/<controller>/")
def viz(controller="cevo"):
    return render_page('main.html', {"controller": controller})

@app.route("/get-data/<controller>", methods = ['GET'])
def data(controller):
    if request.method == "GET":
        data_dir_path = os.path.join(DIR_ROOT, "data", controller)
        data = getSimData(data_dir_path)
        return json.dumps(data)

def getSimData(dir_path):
    d_out = {}
    for fname in G_DATA_FILES:
        dir_path_ = os.path.join(dir_path, fname)
        try:
            if fname == "r_phase.csv":
                d = Data(filepath=dir_path_, is_coords=False, r_phase=True)
            else:
                d = Data(filepath=dir_path_, is_coords=True, r_phase=False)
            key = fname.split(".")[0]
            d_out[key] = d.data
        except Exception as e:
            print(e, " : ", fname)
    return d_out

CTRL_ID = {
    'cevo': 1,
}

# @app.route("/run-sim/<controller>", methods = ['POST'])

# def generate_cmd(data, controller):
    
app.run(port=5000, debug=True)