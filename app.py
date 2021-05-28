from flask import Flask
from flask_migrate import Migrate

from router import router
from database import db

app = Flask(__name__)

# Database info
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://flask_user:password@localhost:5432/flask_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Apply routers to app
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
