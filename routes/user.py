from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from car_rental_system.models.car import Car
from car_rental_system.models.rental import Rental

user = Blueprint('user', __name__)


@user.route('/user_dashboard')
@login_required
def user_dashboard():
    if current_user.role == 'admin':
        flash('Access denied.', 'error')
        return redirect(url_for('main.home'))

    available_cars = Car.get_all_cars()
    return render_template('user_dashboard.html', cars=available_cars)


@user.route('/my_rentals')
@login_required
def my_rentals():
    if current_user.role == 'admin':
        flash('Access denied.', 'error')
        return redirect(url_for('main.home'))

    user_rentals = Rental.get_user_rentals(current_user.id)
    return render_template('my_rentals.html', rentals=user_rentals)
