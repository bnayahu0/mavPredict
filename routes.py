from flask_restful import Resource, reqparse
from flask_expects_json import expects_json
import prediction

schema = {
    "type": "object",
    "properties": {
        "weekday": {"type": "number", "minimum": 0, "maximum": 6},
        "site": {"type": "number", "enum": [710, 720, 760, 770, 287, 790, 550, 200, 540, 650, 740, 750, 709]},
        "hour": {"type": "number", "minimum": 0, "maximum": 23}
    },
    "required": ["weekday", "site", "hour"]
}


class Passage(Resource):
    def get(self):
        return {'message': "Hello World!"}, 200  # return message and 200 OK

    @expects_json(schema)
    def post(self):
        parser = reqparse.RequestParser()  # initialize

        # Weekday - monday is 0, sunday is 6
        parser.add_argument('weekday', required=True)
        # Site - site code at Passage
        parser.add_argument('site', required=True)
        # Hour - hour at the day
        parser.add_argument('hour', required=True)

        args = parser.parse_args()  # parse arguments to dictionary

        # create new object from the variables
        variables = {
            'weekday': 'WEEKDAY_' + args['weekday'],
            'site': 'SITE_ID_' + args['site'],
            'hour': 'HOUR_' + args['hour']
        }

        try:
            return {'prediction': prediction.predict(variables)}, 200  # return data with 200 OK

        except:
            raise Exception(500)

