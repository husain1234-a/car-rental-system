from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from car_rental_system.db import users_collection


class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.name = user_data['name']
        self.email = user_data['email']
        self.password = user_data['password']
        self.role = user_data['role']

    @staticmethod
    def create_user(name, email, password, role="user"):
        hashed_password = generate_password_hash(password)
        user = {
            'name': name,
            'email': email,
            'password': hashed_password,
            'role': role
        }
        return users_collection.insert_one(user).inserted_id

    @staticmethod
    def get_user_by_email(email):
        user_data = users_collection.find_one({'email': email})
        return User(user_data) if user_data else None

    def check_password(self, password):
        return check_password_hash(self.password, password)
