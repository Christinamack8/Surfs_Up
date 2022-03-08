import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
app = Flask(__name__)

@app.route('/')
def index():
    words=['hi','cat','dog']
    return render_template('index.html',data=words)

@app.route('/hello')
def hello():
    return render_template('hello.html')