import requests

# Correct URL of your Flask app endpoint
url = "http://127.0.0.1:5000/score"  # or "http://127.0.0.1:5000/app" if that is your endpoint

# Define client details
client_1 = {"job": "student", "duration": 280, "poutcome": "failure"}
client_2 = {"job": "management", "duration": 400, "poutcome": "success"}

# Send POST requests to the Flask app for each client
response_1 = requests.post(url, json=client_1)
response_2 = requests.post(url, json=client_2)

# Get and output probabilities for each client
result_1 = response_1.json()
result_2 = response_2.json()

print(f"The probability for client 1 (student) is: {result_1['probability']:.4f}")
print(f"The probability for client 2 (management) is: {result_2['probability']:.4f}")
