#Description: this program will create an API that has information about the different water needs of plants

#Importing the libraries
import requests
import json
import flask
from flask import Flask, request, jsonify

#define a dictionary to store the plant information
plantDict = {
    'Plant Potterson': 'water every 2 weeks',
    'Wing_Leaf': 'water every 3 days',
    'Matthew Potitz': 'water every 2 days',
    'Flora Streeter': 'water every 4 days',
    'Chrysanthemum Stemmens': 'water every 5 days',
}

app = Flask(__name__)

@app.route('/plants/<string:name>')
def getPlant(name):
    if name in plantDict:
        return jsonify({name: plantDict[name]})
    else:
        return jsonify({'error': 'Plant not found'})
    
if __name__ == '__main__':
    app.run(debug=True)