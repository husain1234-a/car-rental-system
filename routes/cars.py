from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from car_rental_system.models.car import Car
from car_rental_system.models.rental import Rental
from datetime import datetime

cars = Blueprint('cars', __name__)


@cars.route('/cars')
@login_required
def list_cars():
    all_cars = Car.get_all_cars()
    return render_template('cars.html', cars=all_cars)


@cars.route('/rent_car/<car_id>', methods=['GET', 'POST'])
@login_required
def rent_car(car_id):
    car = Car.get_car_by_id(car_id)
    if request.method == 'POST':
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        Rental.create_rental(current_user.id, car_id, start_date, end_date)
        flash('Car rented successfully.', 'success')
        if 'admin' in current_user.role:
            return redirect(url_for('admin.admin_dashboard'))
        return redirect(url_for('user.user_dashboard'))
    return render_template('rent_car.html', car=car)
