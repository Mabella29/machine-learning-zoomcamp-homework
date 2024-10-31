from flask import Flask, request, jsonify
import pickle


# Load the DictVectorizer and model
with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)

# Initialize the Flask app
app = Flask(__name__)

@app.route('/score', methods=['POST'])
def score():
    client = request.json
    X = dv.transform([client])
    probability = model.predict_proba(X)[0]
    subscription_probability = probability[1]
    return jsonify({'probability': subscription_probability})

if __name__ == '__main__':
    app.run(port=5000)
