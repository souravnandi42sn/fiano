from flask import Flask,jsonify
from flask import render_template
import pandas as pd
from flask import request,redirect,url_for
import matplotlib.pyplot as plt
import numpy as np
from database import preprocessing

app=Flask(__name__)

"""
@app.route('/blog/<float:rev>')
def show_blog(rev):
	return 'Hello_World %f'%rev


@app.route('/<int:Pid>') #here name is the variable which is assigned to below %s datatype as we change in the url
def show_hello(Pid):
	return 'Hello_World %d'%Pid
"""
#graph on development
@app.route('/develope')
def develope():
	return render_template("test.html")





@app.route("/upload_file",methods=["POST"])
def uploade_file():
	file=request.files['myfile']
    # for checking that the input file is a csv file
	if ( file.filename.endswith('.csv')):
		dataset=pd.read_csv(file)
		datalist=preprocessing(dataset)
		print("jsonify",jsonify(datalist))
	return render_template("test.html",datalist=jsonify(datalist))



if __name__=="__main__":
	app.run(debug=True)