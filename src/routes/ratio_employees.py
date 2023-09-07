from flask import Blueprint, jsonify

from models.employees_model import ratioEmployeesModel
main = Blueprint('employee_blueprint', __name__)

@main.route('/')
def get_women_in_goverment():
    try:
        employees = ratioEmployeesModel.get_data()
        return jsonify({'result': employees})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500