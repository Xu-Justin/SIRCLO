from flask import Flask

from routes.berat_bp import berat_bp
from models.Berat import db

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(berat_bp)

db.init_app(app)
with app.app_context():    
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)