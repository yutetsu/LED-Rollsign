from flask_restful import Resource, reqparse
from trainroms import *

class SetRollsign(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('Mode', type=str, required=True, help='Mode is required')
        self.parser.add_argument('Train', type=str, required=True, help='Train is required')
        self.parser.add_argument('Type', type=str, required=False)
        self.parser.add_argument('Dest', type=str, required=False)
        self.parser.add_argument('Line', type=str, required=False)
        self.parser.add_argument('TypeChange', type=str, required=False)
        self.parser.add_argument('Next', type=str, required=False)
        self.parser.add_argument('StopsAt', type=str, required=False)
    
    def get(self):
        args = self.parser.parse_args()
        match args['Train']:
            case "TX3000":
                return TX3000(args).Main()
            case "Laview":
                return Laview(args).Main()
            case "E233-0":
                return E233(args).Main()
            case "E233-1000":
                return E233(args).Main()
            case "E233-5000":
                return E233(args).Main()
            case "E233-6000":
                return E233(args).Main()
            case "E233-7000":
                return E233(args).Main()
            case "E233-8000":
                return E233(args).Main()
            case _:
                return {'message': 'Train ROM not found'}, 404