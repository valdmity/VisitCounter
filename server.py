from flask import Flask, request, make_response
from datetime import datetime
import database as db


app = Flask(__name__)


@app.route('/<id>')
def get(id):
    user_id = get_user_id(id)
    db.add_to_db(user_id, str(datetime.utcnow())[:19], parse_browser(request.user_agent.string))
    return get_response(user_id)


def get_user_id(id: str):
    if id != '0': return id 
    return str(len(db.get_all_ids()) + 1)


def get_response(user_id: str):
    response = make_response(user_id)
    response.headers = {"Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Credentials": True}
    return response


def parse_browser(headers):
    if 'OPR' in headers or 'Opera' in headers:
        return 'Opera'
    if 'Safari' in headers and 'Chrome' not in headers:
        return 'Safari'
    if 'Edg' in headers:
        return 'Edge'
    if 'Firefox' in headers:
        return 'Firefox'
    return 'Chrome'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
