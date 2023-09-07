from flask import Blueprint, jsonify

from models.women_model import WomenInGovermentModel
main = Blueprint('women_blueprint', __name__)

@main.route('/')
def get_women_in_goverment():
    try:
        wig = WomenInGovermentModel.get_data()
        return jsonify({'result': wig})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
