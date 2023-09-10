from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import base64
from flask import session
from flask import jsonify
from flask import redirect
from flask import url_for




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:stivemok@localhost/easy'
db = SQLAlchemy(app)

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
   
with app.app_context():
    # Create all tables in the database which don't exist yet
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

    def __init__(self, pickup_date, pickup_location, dropoff_date, dropoff_location, vehicle_type):
        self.pickup_date = pickup_date
        self.pickup_location = pickup_location
        self.dropoff_date = dropoff_date
        self.dropoff_location = dropoff_location
        self.vehicle_type = vehicle_type

with app.app_context():
    # Create all tables in the database which don't exist yet
    db.create_all()


#This code defines a new User class that inherits from db.Model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

with app.app_context():
    # Create all tables in the database which don't exist yet
    db.create_all()

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

with app.app_context():
    # Create all tables in the database which don't exist yet
    db.create_all()

with app.app_context():
    # add payment methods to the database if they don't already exist
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

@app.route('/VehicelRegistration')
def VehicelRegistration():
    return render_template('VehicelRegistration.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/AdminRegistration')
def AmdinRegistration():
    return render_template('AdminRegistration.html')

@app.route('/AddCar')
def AddCar():
    return render_template('AddCar.html')

@app.route('/admin')
def admin():
    return render_template('AdminPage.html')

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
    # Your code for processing the payment goes here
    return render_template('PaymentConfirmation.html')


#check if the provided email and password match
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return 'success'
    else:
        return 'failure'

#check if the password and comfirmpassword match and add new user in datanase
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
    booking = Booking.query.filter_by(pickup_date=pickup_date, pickup_location=pickup_location, dropoff_date=dropoff_date, dropoff_location=dropoff_location).first()
    if booking:
        # booking already existsBB
        available_cars = Car.query.filter_by(available=True).all()
        available_cars_list = [car.to_dict() for car in available_cars]
        return jsonify({'status': 'error', 'message': 'Already booked', 'available_cars': available_cars_list})
    else:
        # create new booking
        new_booking = Booking(pickup_date=pickup_date, pickup_location=pickup_location, dropoff_date=dropoff_date, dropoff_location=dropoff_location, vehicle_type=vehicle_type)
        db.session.add(new_booking)
        db.session.commit()
        payment_methods = PaymentMethod.query.all()
        payment_methods_list = [method.to_dict() for method in payment_methods]
        return jsonify({'status': 'success', 'message': 'process payment method', 'payment_methods': payment_methods_list})


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
