import os

from flask import Flask, request

from snippet.lib import predict_ids


app = Flask(__name__)
DEBUG = bool(os.getenv('DEBUG', True))
PORT = int(os.getenv('PORT', 8080))


@app.route('/api/v1/ping')
def ping():
    return 'pong'


@app.route('/api/v1/predict', methods=['POST'])
def predict():
    content = request.json
    print(content)
    count = content['count']

    rec_list = predict_ids(count)

    return {
        'code': 'OK',
        'message': '',
        'result': rec_list
    }


if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
