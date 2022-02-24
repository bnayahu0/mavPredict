from flask import Flask
from flask_restful import Api
import routes


app = Flask(__name__)
api = Api(app)


api.add_resource(routes.Passage, '/passage')


@app.errorhandler(404)
def invalid_route(e):
    return "Invalid Route", 404


@app.errorhandler(400)
def invalid_route(e):
    return "Json Schema Validation Error", 400


@app.errorhandler(500)
def invalid_route(e):
    return "Internal Server Error", 500


app.run("0.0.0.0",5000)  # run our Flask app at port 5000
