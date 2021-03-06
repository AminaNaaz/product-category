from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import pickle


# load the model from disk
filename = 'nlp_model.pkl'
clf= pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
app = Flask(__name__

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    'if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		

        my_prediction = rf.predict(data)	
        my_prediction= v[predicted[0]]
     
	return render_template('result.html',prediction = my_prediction)




if __name__ == "__main__":
    app.run(debug=True)s