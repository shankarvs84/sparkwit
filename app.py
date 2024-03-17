import os

from flask import request, jsonify

from api import app
from api_query import get_api_query_response


@app.route("/ping", methods=["POST"])
def esg_query():
    data = request.get_json()
    print('Query request: ', data)
    answer = get_api_query_response(data)
    print('Answer: ', answer)
    status_code = 200 if answer else 400
    return jsonify(answer), status_code


if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
