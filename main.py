from flask import Flask,request,jsonify


# import pandas as pd
import numpy as np


import pickle
app = Flask(__name__)
lrmodel = pickle.load(open('models','rb'))


@app.route('/')
def hom():
    return "ha pn chalu kay"

@app.route('/find',methods=['POST'])
def main():
    Marks = request.form.get('Marks')
    Stamina = request.form.get('Stamina')
    Present = request.form.get('Present')
    Absent = request.form.get('Absent')
    Avg = request.form.get('Avg')
    Score = request.form.get('Score')
    Project = request.form.get('Project')
    Practical = request.form.get('Practical')
    Internship = request.form.get('Internship')
    Unit = request.form.get('Unit')

    input_query = np.array([[Marks,Stamina,Present,Absent,Avg,Score,Project,Practical,Internship,Unit]],dtype=float)
    result = lrmodel.predict(input_query)[0]
    return jsonify({'Status': str(result)})


if __name__ == '__main__':
    app.run(debug=True)
