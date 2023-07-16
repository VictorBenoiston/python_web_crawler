import requests
from flask import Flask, request, jsonify, make_response
from website_scraper import buscar_processo


app = Flask(__name__)

# app.config['RESTFUL_JSON'] = {
#     'ensure_ascii': False
# }

@app.route('/search', methods=['GET'])
def get_data():
    data = request.json
    nuProcess = data.get('nuProcesso')

    try:
        data = buscar_processo(nuProcess)
        return make_response(
            data
        )
    except Exception as err:
        error_message = "There are no information available regarding the given parameters. Try again."
        return make_response(error_message, 400)

app.run()



