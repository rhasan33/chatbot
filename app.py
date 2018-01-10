from flask import Flask
from json import dumps
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    data = {
        "success": True,
        "message": "Exploring Graph API."
    }
    response = app.response_class(
        response=dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=os.environ.get("DEBUG_MODE", True))
