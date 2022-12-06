from flask import Flask, request, make_response
from datetime import datetime
import database as db

app = Flask(__name__)


@app.route('/<id>')
def get(id):
    user_id = get_user_id(id)
    db.add_to_db(user_id, str(datetime.utcnow())[:19])
    return get_response(user_id)


def get_user_id(id: str):
    if id != '0': return id
    return len(db.get_all_values().keys())


def get_response(user_id: str):
    response = make_response(user_id)
    response.headers = {"Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Credentials": True}
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
