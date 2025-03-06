from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from car_rental_system.models.car import Car
from car_rental_system.models.rental import Rental

admin = Blueprint('admin', __name__)


@admin.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied.', 'error')
        return redirect(url_for('main.home'))
    return render_template('admin_dashboard.html')


@admin.route('/add_car', methods=['GET', 'POST'])
@login_required
def add_car():
    if current_user.role != 'admin':
        flash('Access denied.', 'error')
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        car_name = request.form['car_name']
        car_number = request.form['car_number']
        car_type = request.form['car_type']
        car_price = float(request.form['car_price'])
        Car.create_car(car_name, car_number, car_type, car_price)
        flash('Car added successfully.', 'success')
        return redirect(url_for('admin.admin_dashboard'))

    return render_template('add_car.html')


@admin.route('/show_rented_cars')
@login_required
def show_rented_cars():
    if current_user.role != 'admin':
        flash('Access denied.', 'error')
        return redirect(url_for('main.home'))

    rented_cars = Rental.get_active_rentals()
    return render_template('rented_cars.html', rentals=rented_cars)
