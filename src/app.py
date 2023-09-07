from flask import Flask

from config import config

# routes
from routes import women_in_goverment, ratio_employees

app = Flask(__name__)

def page_not_found(error):
    return '<h1>Not found page</h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(women_in_goverment.main, url_prefix='/api/women-in-goverment')
    
    app.register_blueprint(ratio_employees.main, 
                           url_prefix='/api/ratio-employees')

    # Error handling
    app.register_error_handler(404, page_not_found)
    app.run()
