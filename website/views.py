from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Employees
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        name = request.form.get('name')
        job_position = request.form.get('job_position')
        email = request.form.get('email')
        starting_date = request.form.get('starting_date')
        ending_date = request.form.get('ending_date')#Gets the inputs from the HTML 

        if len(name) < 1:
            flash('Name is too short!', category='error') 
        else:
            new_input = Employees(name=name, job_position=job_position, email=email, starting_date=starting_date, ending_date=ending_date, user_id=current_user.id)
            db.session.add(new_input) #adding the inputs to the database 
            db.session.commit()
            flash('Employee added!', category='success')
            return render_template("home.html", data=Employees.query.all(), user=current_user, submitted=True)

    return render_template("home.html", data=Employees.query.all(), user=current_user, submitted=False)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    employee = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    employeeID = employee['employeeID']
    employee = Employees.query.get(employeeID)
    if employee:
        if employee.user_id == current_user.id:
            db.session.delete(employee)
            db.session.commit()

    return jsonify({})