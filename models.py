from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meet_id = db.Column(db.Integer)
    meet_path = db.Column(db.String(255))
    federation = db.Column(db.String(255))
    date = db.Column(db.String(20))  # Assuming date is a string for now
    meet_country = db.Column(db.String(100))
    meet_state = db.Column(db.String(100))
    meet_town = db.Column(db.String(100))
    meet_name = db.Column(db.String(255))
    # Powerlift data fields
    sn = db.Column(db.Integer)
    name = db.Column(db.String(255))
    sex = db.Column(db.String(1))
    equipment = db.Column(db.String(255))
    age = db.Column(db.Integer)
    division = db.Column(db.String(255))
    bodyweight_kg = db.Column(db.Float)
    weight_class_kg = db.Column(db.Integer)
    squat4_kg = db.Column(db.Float)
    best_squat_kg = db.Column(db.Float)
    bench4_kg = db.Column(db.Float)
    best_bench_kg = db.Column(db.Float)
    deadlift4_kg = db.Column(db.Float)
    best_deadlift_kg = db.Column(db.Float)
    total_kg = db.Column(db.Float)
    place = db.Column(db.Integer)
    wilks = db.Column(db.Float)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
