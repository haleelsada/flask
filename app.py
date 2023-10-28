from flask import Flask, request, jsonify

app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/test',methods=['POST','GET'])
def sentanalase():
	print('api called')
	
	
	return jsonify({'result':'result'})

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
 

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
