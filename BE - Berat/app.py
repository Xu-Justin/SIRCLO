from flask import Flask

from routes.berat_bp import berat_bp
from models.Berat import db

def create_app(database = './database.db'):
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.update({ "SQLALCHEMY_DATABASE_URI": 'sqlite:///' + database })
    app.register_blueprint(berat_bp)

    db.init_app(app)
    with app.app_context():    
        db.create_all()
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)