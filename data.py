from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hailmary@localhost/easy'
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
    idpassport = db.Column(db.String(255))
    carreg = db.Column(db.String(255))

@app.route('/vehicel')
def registration():
    return render_template('registration.html')

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

    # Get the values of the new form fields for ID/Passport and Car Registration
    idpassport = request.files['idpassport'].filename
    carreg = request.files['carreg'].filename

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
        carreg=carreg
    )

    # Add the new FormData object to the database session and commit the changes
    db.session.add(form_data)
    db.session.commit()

    return 'Data inserted successfully'

if __name__ == '__main__':
    app.run()
