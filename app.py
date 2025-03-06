from bson import ObjectId
from flask import Flask
from flask_login import LoginManager

from car_rental_system.db import users_collection
from models.user import User
from routes.auth import auth
from routes.cars import cars
from routes.rentals import rentals
from routes.main import main
from routes.admin import admin
from routes.user import user

#added comments
app = Flask(__name__)
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # Convert user_id from string to ObjectId
    try:
        user_id = ObjectId(user_id)
    except Exception as e:
        print(f"Error converting user_id to ObjectId: {e}")
        return None

    user_data = users_collection.find_one({'_id': user_id})
    return User(user_data) if user_data else None


app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(cars)
app.register_blueprint(rentals)
app.register_blueprint(admin)
app.register_blueprint(user)


if __name__ == '__main__':
    app.run()
