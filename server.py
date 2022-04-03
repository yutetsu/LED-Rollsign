from flask import Flask
from flask_restful import Api
from resources import Rollsign

app = Flask(__name__)
api = Api(app)

# Rollsing Resource
api.add_resource(Rollsign, '/rollsign')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)