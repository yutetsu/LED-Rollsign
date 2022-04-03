from flask_restful import Resource, reqparse
from trainroms import *
from hardware import LedDriver


class Rollsign(Resource):
    def __init__(self) -> None:
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('mode', type=str, required=True, help='Mode is required')
        self.parser.add_argument('train', type=str, required=True, help='Train is required')
        self.parser.add_argument('type', type=str, required=False)
        self.parser.add_argument('dest', type=str, required=False)
        self.parser.add_argument('line', type=str, required=False)
        self.parser.add_argument('type_change', type=str, required=False)
        self.parser.add_argument('next', type=str, required=False)
        self.parser.add_argument('stops_at', type=str, required=False)
    
    def post(self):
        args = self.parser.parse_args()
        match args['train']:
            case "TX3000":
                return Tx3000(args).main()
            case "Laview":
                return Laview(args).main()
            case "E233-0":
                return E233(args).main()
            case "E233-1000":
                return E233(args).main()
            case "E233-5000":
                return E233(args).main()
            case "E233-6000":
                return E233(args).main()
            case "E233-7000":
                return E233(args).main()
            case "E233-8000":
                return E233(args).main()
            case _:
                return {'message': 'Train ROM not found'}, 404

    def delete(self):
        LedDriver().clear()
        return {'message': 'Rollsign cleared'}, 200