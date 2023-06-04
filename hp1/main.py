# Importing essential libraries
from flask import Flask, render_template, request
import numpy as np
import pickle


# Load the  model
filename = 'networkmodel.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        bed = int(request.form['bed'])
        bath = int(request.form['bath'])
        sqftliv = int(request.form['sqftliv'])
        sqftlot = int(request.form['sqftlot'])
        floors = int(request.form['floors'])
        waterfront = int(request.form['waterfront'])
        condition = int(request.form['condition'])
        year = int(request.form['year'])
        
        data = np.array([[bed, bath, sqftliv, sqftlot, floors, waterfront, condition, year]])
        my_prediction = model.predict(data)
        
        return str(my_prediction)


if __name__ == '__main__':
	app.run(debug=True) 
