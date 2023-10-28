import pickle 
import spacy
from flask import Flask,request
from sklearn.feature_extraction.text import TfidfVectorizer


nlp = spacy.load("en_core_web_sm")

happiness='happiness.pkl'
anger='anger.pkl'
love='love.pkl'  
nuetral='nuetral.pkl'  
saddness='saddness.pkl' 

vect='vectorizer.pkl'
vectorizer = TfidfVectorizer()


with open(happiness, 'rb') as file:  
    happiness = pickle.load(file)
with open(anger, 'rb') as file:  
    anger = pickle.load(file)
with open(love, 'rb') as file:  
    love = pickle.load(file)
with open(nuetral, 'rb') as file:  
    nuetral = pickle.load(file)
with open(saddness, 'rb') as file:  
    saddness = pickle.load(file)
with open(vect, 'rb') as file:  
    vectorizer = pickle.load(file)


def emotion(text):
	input_processed = ' '.join([token.lemma_ for token in nlp(text) if not token.is_stop])
	input_vectorized = vectorizer.transform([input_processed])
	return {'happiness':happiness.predict(input_vectorized)[0],'saddness':saddness.predict(input_vectorized)[0],'anger':anger.predict(input_vectorized)[0],'love':love.predict(input_vectorized)[0],'nuetral':nuetral.predict(input_vectorized)[0]}
	
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/test',methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        text = request.form['input']
        return emotion(text)
    return 'provide query'
    
if __name__ == '__main__':
    
    app.run(debug=True)
