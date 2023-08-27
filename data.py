from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import base64


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:stivemok@localhost/easy'
db = SQLAlchemy(app)

# Define a model for the database table
class FormData(db.Model):
    __tablename__ = 'vregister'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    mname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    vehicle = db.Column(db.String(255))
    year = db.Column(db.Integer)
    idpassport = db.Column(db.LargeBinary)
    carreg = db.Column(db.LargeBinary)
    photo1 = db.Column(db.LargeBinary)
    photo2 = db.Column(db.LargeBinary)
    submissionDate = db.Column(db.DateTime)

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

@app.route('/AmdinRegistration')
def AmdinRegistration():
    return render_template('AmdinRegistration.html')


@app.route('/search-vehicle', methods=['POST'])
def search_vehicle():
    vehicle = request.form['vehicle']
    vehicles = FormData.query.filter_by(vehicle=vehicle).all()

    for vehicle in vehicles:
        vehicle.photo1_base64 = base64.b64encode(vehicle.photo1).decode('utf-8')
        vehicle.photo2_base64 = base64.b64encode(vehicle.photo2).decode('utf-8')

    return render_template('searchResults.html', vehicles=vehicles)

@app.route('/search-results', methods=['GET'])
def display_search_results():
    return render_template('searchResults.html')


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
    # Get the current date and time
    currentDate = datetime.now()

    # Create a new FormData object with the form data
    form_data = FormData(
        fname=fname,
        mname=mname,
        lname=lname,
        phone=phone,
        email=email,
        vehicle=vehicle,
        year=year,
        idpassport=idpassport,
        carreg=carreg,
        photo1=photo1,
        photo2=photo2,
        submissionDate=currentDate
    )

    # Add the new FormData object to the database session and commit the changes
    db.session.add(form_data)
    db.session.commit()

    return 'Data inserted successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
