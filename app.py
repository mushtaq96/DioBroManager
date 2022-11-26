from flask import Flask, jsonify, request
# from livereload import Server
from dotenv import load_dotenv
import json
from src.person.client import getUser, createPerson
from src.person.obj import Person

load_dotenv()

app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})



@app.route('/hello')
def hello():
    return 'Hello'

#crud for person
@app.route('/person/<name>')
def user(name):
    response = getUser(name)
    if response is None:
        return jsonify({'error':400})
    return jsonify(response)

@app.route('/person', methods=['POST'])
def post_person():
    # create a new person obj from req body
    body = request.get_json()
    # person = Person(**body)
    response = createPerson(body)
    if response == None:
        jsonify({'success':True})
    return jsonify({'failure':False})


if __name__ == '__main__':
    app.run(host='0.0.0.0')