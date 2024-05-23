import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/profiles', methods=['GET'])
def get_profiles():
    # Call randomuser API to generate user data
    response = requests.get('https://randomuser.me/api/?results=20')
    data = response.json()['results']
    
    # Generate profile descriptions
    profiles = []
    for user in data:
        profile = {
            'name': f"{user['name']['first']} {user['name']['last']}",
            'age': user['dob']['age'],
            'photo': user['picture']['large'],
            'city': user['location']['city'],
            'country': user['location']['country'],
            'bio': f"I am {user['name']['first']}, {user['dob']['age']} years old, from {user['location']['city']}."
        }
        profiles.append(profile)
    
    # Return profiles
    return jsonify(profiles)

# Point d'entrée de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)