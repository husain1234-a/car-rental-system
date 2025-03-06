from bson import ObjectId
from datetime import datetime, timedelta
from car_rental_system.db import cars_collection, rentals_collection


class Rental:
    @staticmethod
    def create_rental(user_id, car_id, start_date, end_date):
        rental = {
            'user_id': ObjectId(user_id),
            'car_id': ObjectId(car_id),
            'start_date': start_date,
            'end_date': end_date,
            'total_amount': Rental.calculate_total_amount(car_id, start_date, end_date),
            'status': 'active'
        }
        rental_id = rentals_collection.insert_one(rental).inserted_id
        Rental.update_car_availability(car_id, False)
        return rental_id

    @staticmethod
    def update_car_availability(car_id, availability):
        cars_collection.update_one({'_id': ObjectId(car_id)}, {'$set': {'availability': availability}})

    @staticmethod
    def calculate_total_amount(car_id, start_date, end_date):
        car = cars_collection.find_one({'_id': ObjectId(car_id)})
        daily_rent = car['daily_rent']
        num_days = 1 if (end_date - start_date).days == 0 else (end_date - start_date).days
        return daily_rent * num_days

    @staticmethod
    def update_rental_total_amount(rental_id, additional_days):
        rental = rentals_collection.find_one({'_id': ObjectId(rental_id)})
        total_amount = rental['total_amount']
        additional_amount = additional_days * 116.34
        rentals_collection.update_one({'_id': ObjectId(rental_id)},
                                      {'$set': {'total_amount': total_amount + additional_amount}})

    @staticmethod
    def get_user_rentals(user_id):
        return list(rentals_collection.find({'user_id': ObjectId(user_id)}))

    def return_car(rental_id):
        rental = rentals_collection.find_one({'_id': ObjectId(rental_id)})
        if rental:
            current_date = datetime.now().date()
            end_date = rental['end_date'].date() if isinstance(rental['end_date'], datetime) else rental['end_date']

            if current_date > end_date:
                additional_days = (current_date - end_date).days
                Rental.update_rental_total_amount(rental_id, additional_days)

            Rental.update_car_availability(rental['car_id'], True)
            rentals_collection.update_one({'_id': ObjectId(rental_id)}, {'$set': {'status': 'returned'}})
            return True
        return False

    @staticmethod
    def get_active_rentals():
        return list(rentals_collection.find({'status': 'active'}))
