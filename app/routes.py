from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import User, Workout

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    workouts = Workout.query.all()
    return render_template('index.html', workouts=workouts)

@bp.route('/add_workout', methods=['GET', 'POST'])
def add_workout():
    if request.method == 'POST':
        exercise = request.form['exercise']
        sets = int(request.form['sets'])
        reps = int(request.form['reps'])
        weight = float(request.form['weight']) if request.form['weight'] else None
        user_id = 1  # For simplicity, assume user 1

        workout = Workout(exercise=exercise, sets=sets, reps=reps, weight=weight, user_id=user_id)
        db.session.add(workout)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_workout.html')