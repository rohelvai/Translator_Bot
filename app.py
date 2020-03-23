from flask import Flask, request
import os, sys, json
from pprint import pprint
from main import controller


app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    data = request.args.to_dict()
    if request.args.get('last clicked button name') == 'Get Started' and request.args.get('last user freeform input') == '':
        message = '/start'
    else:
        message = request.args.get('last user freeform input')
    user_id = request.args.get('messenger user id')
    first_name = request.args.get('first name')
    last_name = request.args.get('last name')
    name = first_name+' '+last_name if first_name != last_name else last_name
    log(data)
    return send_message(user_id, message, name)


def send_message(user_id, message, name):
    return json.dumps({"messages": [{"text": controller(message, user_id, name)}]})


def log(data):
    pprint(data)
    sys.stdout.flush()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
