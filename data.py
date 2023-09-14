#!/usr/bin/python3
"""Flask: a micro web framework to build web application
   request: access incomming request data
render_template: render HTML templetes with dynamic content for the web application"""
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy # ORM that simplifies database interactions
from datetime import datetime # provides classes for dates & time
import base64 # provides functions for encoding and decoding binary data as base64
from flask import session # to store user data that persists across multiple requests
from flask import jsonify # to create a JSON response from a python dictionary or other JSON-serializable data
from flask import redirect # to reedirect the user to a different URL or route
from flask import url_for # generates URL for the routes
from database import db, init_app


# Initializing and configuring a Flask application
app = Flask(__name__) # creates a Flaslk web application instance
app.secret_key = 'secret' # sets a secret key for securing cookies and session data
init_app(app)

# Define a model for the database table
class FormData(db.Model):
    __tablename__ = 'vregister'
    CustomerId = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    mname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    vehicle = db.Column(db.String(255))
    year = db.Column(db.Integer)
    idpassport = db.Column(db.LargeBinary((2**32)-1))
    carreg = db.Column(db.LargeBinary((2**32)-1))
    photo1 = db.Column(db.LargeBinary((2**32)-1))
    photo2 = db.Column(db.LargeBinary((2**32)-1))
    PlateNo = db.Column(db.String(255))
    make = db.Column(db.String(255))
    model = db.Column(db.String(255))
    color = db.Column(db.String(255))
    price = db.Column(db.String(255)) 
    condition = db.Column(db.String(255))
    submissionDate = db.Column(db.DateTime)

with app.app_context():
    # Create all tables in the database which don't exist yet
    db.create_all()

# Define SQLAlchemy model class for the database table
class Car(db.Model):
    __tablename__ = 'vehicle'
    VehicleId = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(255))
    model = db.Column(db.String(255))
    year = db.Column(db.Integer)
    condition = db.Column(db.String(255))
    price = db.Column(db.String(255))
    color = db.Column(db.String(255))
    photo1 = db.Column(db.LargeBinary((2**32)-1))
    photo2 = db.Column(db.LargeBinary((2**32)-1))
    PlateNo = db.Column(db.String(255))
    vehicle = db.Column(db.String(255))
    available = db.Column(db.Boolean, default=True)

# Create all tables in the database which don't exist yet
with app.app_context():
    db.create_all()


# Define a model for the booking table
class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    pickup_date = db.Column(db.Date, nullable=False)
    pickup_location = db.Column(db.String(255), nullable=False)
    dropoff_date = db.Column(db.Date, nullable=False)
    dropoff_location = db.Column(db.String(255), nullable=False)
    vehicle_type = db.Column(db.String(255), nullable=False)

# Create all tables in the database which don't exist yet
with app.app_context():
    db.create_all()


#This code defines a new User class that inherits from db.Model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Create all tables in the database which don't exist yet
with app.app_context():
    db.create_all()

# creating and populating a database table
class PaymentMethod(db.Model):
    __tablename__ = 'payment_methods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

# Create all tables in the database which don't exist yet
with app.app_context():
    db.create_all()

# add payment methods to the database if they don't already exist
with app.app_context():
    db.create_all()
    if not PaymentMethod.query.filter_by(name='Credit Card').first():
        credit_card = PaymentMethod(name='Credit Card', description='Pay with your credit card')
        db.session.add(credit_card)
    if not PaymentMethod.query.filter_by(name='Debit Card').first():
        debit_card = PaymentMethod(name='Debit Card', description='Pay with your debit card')
        db.session.add(debit_card)
    if not PaymentMethod.query.filter_by(name='PayPal').first():
        paypal = PaymentMethod(name='PayPal', description='Pay with your PayPal account')
        db.session.add(paypal)
    db.session.commit()


# Flask routes in the web application
@app.route('/easy')
def home():
    return render_template('index.html')

@app.route('/vehicles')
def vehicles():
    return render_template('vehicles.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')

#check if the provided email and password match
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        session['logged_in'] = True
        return 'success'
    else:
        return 'failure'


@app.route('/admin')
def admin():
    if 'logged_in' in session:
        return render_template('AdminPage.html')
    else:
        return redirect(url_for('AdminLogin'))

@app.route('/VehicelRegistration')
def VehicelRegistration():
    return render_template('VehicelRegistration.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/AdminRegistration')
def AmdinRegistration():
    return render_template('AdminRegistration.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('AdminLogin'))

@app.route('/AddCar')
def AddCar():
    return render_template('AddCar.html')

@app.route('/booking')
def booking():
    return render_template('/BookVehicle.html')


@app.route('/Orders')
def Orders():
    return render_template('/Orders.html')

@app.route('/available-cars')
def available_cars():
    cars = Car.query.filter_by(available=True).all()
    return render_template('AvailableCars.html', vehicle=vehicle)

@app.route('/payment-methods')
def payment_methods():
    # retrieve available payment methods from the database
    payment_methods = PaymentMethod.query.all()
    payment_methods_list = [method.to_dict() for method in payment_methods]
    return render_template('PaymentMethods.html', payment_methods=payment_methods_list)

@app.route('/process-payment', methods=['POST'])
def process_payment():
    return render_template('PaymentConfirmation.html')


#check if the password and comfirmpassword match and add new user in database
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        confirm_pass = request.form['confirm-pass']
        if password == confirm_pass:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return 'Email already taken!'
            else:
                user = User(email=email, password=password)
                db.session.add(user)
                db.session.commit()
                return 'Registration successful!'
        else:
            return 'Password and Confirm Password must be identical!'
    return render_template('AmdinRegistration.html')

#manage-user for admin page
@app.route('/manageuser')
def manageuser():
    users = User.query.all()
    return render_template('manage-user.html', users=users)


#route for handling booking
@app.route('/search-vehicle', methods=['POST'])
def search_vehicle():
    data = request.get_json()
    pickup_date = data['pickup_date']
    pickup_location = data['pickup_location']
    dropoff_date = data['dropoff_date']
    dropoff_location = data['dropoff_location']
    vehicle_type = data['vehicle_type']

    # check if booking is available
    booking = Booking.query.filter_by(pickup_date=pickup_date,
                                      pickup_location=pickup_location,
                                      dropoff_date=dropoff_date,
                                      dropoff_location=dropoff_location).first()
    if booking:
        # booking already exists
        available_cars = Car.query.filter_by(available=True).all()
        return  'Booking already exists check the vehicle page'
    else:
        # redirect to vehicle page
        return redirect(url_for('vehicles'))


@app.route('/get-images', methods=['POST'])
def get_images():
    index = request.form['index']
    car = Car.query.get(index)
    if car:
        image_data1 = car.photo1
        image_src1 = f"data:image/jpeg;base64,{base64.b64encode(image_data1).decode('utf-8')}"
        image_data2 = car.photo2
        image_src2 = f"data:image/jpeg;base64,{base64.b64encode(image_data2).decode('utf-8')}"
        return jsonify({'imageSrc1': image_src1, 'imageSrc2': image_src2})
    else:
        return jsonify({'error': 'Car not found'})


@app.route('/get-vehicle-info', methods=['POST'])
def get_vehicle_info():
    index = request.form['index']
    car = Car.query.get(index)
    if car:
        make = car.make
        model = car.model
        year = car.year
        condition = car.condition
        color = car.color
        price = car.price
        return jsonify({'make': make, 'model': model, 'year': year, 'condition': condition, 'color': color, 'price': price})
    else:
        return jsonify({'error': 'Car not found'})

#habdle booking vehicle
@app.route('/book-vehicle', methods=['POST'])
def book_vehicle():
    data = request.get_json()
    pickup_date = datetime.strptime(data['pickup_date'], '%Y-%m-%d').date()
    dropoff_date = datetime.strptime(data['dropoff_date'], '%Y-%m-%d').date()
    booking = Booking.query.filter_by(
        pickup_date=pickup_date,
        pickup_location=data['pickup_location'],
        dropoff_date=dropoff_date,
        dropoff_location=data['dropoff_location'],
        vehicle_type=data['vehicle_type']
    ).first()
    if booking:
        return jsonify({'bookingExists': True})
    else:
        new_booking = Booking(
            pickup_date=pickup_date,
            pickup_location=data['pickup_location'],
            dropoff_date=dropoff_date,
            dropoff_location=data['dropoff_location'],
            vehicle_type=data['vehicle_type']
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'bookingSuccess': True})



#handle to retrive all bookings
@app.route('/all-bookings', methods=['GET'])
def get_all_bookings():
    bookings = Booking.query.all()
    all_bookings = []
    for booking in bookings:
        booking_data = {
            'pickup_date': booking.pickup_date.strftime('%Y-%m-%d'),
            'pickup_location': booking.pickup_location,
            'dropoff_date': booking.dropoff_date.strftime('%Y-%m-%d'),
            'dropoff_location': booking.dropoff_location,
            'vehicle_type': booking.vehicle_type
        }
        all_bookings.append(booking_data)
    return jsonify({'bookings': all_bookings})



@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Get the form data from the POST request
    fname = request.form['fname']
    mname = request.form['mname']
    lname = request.form['lname']
    phone = request.form['phone']
    email = request.form['email']
    vehicle = request.form['vehicle']
    year = request.form['year']

    # Get the values of the new form fields for ID/Passport,Car Registration,car photo
    idpassport = request.files['idpassport'].read()
    carreg = request.files['carreg'].read()
    photo1 = request.files['photo1'].read()
    photo2 = request.files['photo2'].read()
    currentDate = datetime.now()
    PlateNo = request.form['PlateNo']
    make = request.form['make']
    model = request.form['model']
    color = request.form['color']
    price = request.form['price']
    condition = request.form['condition']

# Check if a FormData object with the same Plate number already exists in the database
    existing_form_data = FormData.query.filter_by(PlateNo=PlateNo).first()

    if existing_form_data:
        # If a FormData object with the same Plate number already exists, return a message saying "Already registered"
        return 'Already registered'
    else:
        # If a FormData object with the same Plate number does not exist, create a new FormData object with the form data

    # Create a new FormData object with the form data
     form_data = FormData(
         fname=fname,
         mname=mname,
         lname=lname,
         phone=phone,
         email=email,
         idpassport=idpassport,
         submissionDate=currentDate,
         PlateNo=PlateNo,
         make=make,
         model=model,
         color=color,
         price=price,
         vehicle=vehicle,
         year=year,
         carreg=carreg,
         photo1=photo1,
         photo2=photo2,
         condition=condition
     )

# Add the new FormData object to the database session and commit the changes
    db.session.add(form_data)
    db.session.commit()

# Check if a Car object with the same Plate number already exists in the database
    existing_car = Car.query.filter_by(PlateNo=PlateNo).first()

    if not existing_car:
      # If a Car object with the same Plate number does not exist, create a new Car object with the form data

         # Create a new Car object with the form data
          new_car = Car(
             make=make,
             model=model,
             year=year,
             condition=condition,
             color=color,
             price=price,
             photo1=photo1,
             photo2=photo2,
             PlateNo=PlateNo
           )

          # Add the new Car object to the database session and commit the changes
          db.session.add(new_car)
          db.session.commit()

    return 'Registered  successfully'


@app.route('/submit_car', methods=['POST'])
def submit_car():
    make = request.form['make']
    model = request.form['model']
    year = request.form['year']
    condition = request.form['condition']
    color = request.form['color']
    price = request.form['price']
    PlateNo = request.form['PlateNo']
    vehicle = request.form['vehicle']
    # Get the uploaded files for Car Photo 1 and Car Photo 2
    photo1 = request.files['photo1'].read()
    photo2 = request.files['photo2'].read()

    # Check if the same plate number is already registered
    existing_car = Car.query.filter_by(PlateNo=PlateNo).first()
    if existing_car:
        return 'already exist'

    else:
       # Create a new Car object and add it to the database
       car = Car(make=make,
             model=model,
             year=year,
             condition=condition,
             color=color,
             price=price,
             photo1=photo1,
             photo2=photo2,
             PlateNo= PlateNo)

       db.session.add(car)
       db.session.commit()
       return 'success'


# Run Flask web application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
