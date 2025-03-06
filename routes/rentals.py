from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from car_rental_system.models.rental import Rental
from car_rental_system.models.car import Car

rentals = Blueprint('rentals', __name__)


@rentals.route('/my_rentals')
@login_required
def my_rentals():
    user_rentals = Rental.get_user_rentals(current_user.id)

    # Enrich rentals with car details
    rentals_with_cars = []
    for rental in user_rentals:
        car = Car.get_car_by_id(rental['car_id'])
        rental['car'] = car
        rentals_with_cars.append(rental)

    return render_template('my_rentals.html', rentals=rentals_with_cars)


@rentals.route('/return_car/<rental_id>', methods=['POST'])
@login_required
def return_car(rental_id):
    success = Rental.return_car(rental_id)
    if success:
        flash('Car returned successfully.', 'success')
    else:
        flash('Failed to return car. Please try again.', 'error')
    return redirect(url_for('rentals.my_rentals'))
