from flask_restful import Resource, reqparse
from hardware.LED import LED_Driver

class ClearRollsign(Resource):
    def get(self):
        LED_Driver().Clear()
        return {'message': 'Rollsign cleared'}, 200
