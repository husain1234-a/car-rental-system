from bson import ObjectId

from car_rental_system.db import cars_collection


class Car:
    @staticmethod
    def create_car(car_name, car_number, car_type, car_price):
        car = {
            'car_name': car_name,
            'car_number': car_number,
            'car_type': car_type,
            'daily_rent': car_price,
            'availability': True
        }
        return cars_collection.insert_one(car).inserted_id

    @staticmethod
    def get_all_cars():
        return list(cars_collection.find())

    @staticmethod
    def get_car_by_id(car_id):
        return cars_collection.find_one({'_id': ObjectId(car_id)})
