from flask import Flask, request, jsonify
from transformers import pipeline
app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/test',methods=['POST','GET'])
def sentanalase():
	print('api called')
	classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=5)

	sentences = ["Today was a rough day from the start. I woke up late, missed my bus"]
	
	model_outputs = classifier(sentences)
	print(model_outputs[0])
	
	return jsonify({'result':result})

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
 

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
