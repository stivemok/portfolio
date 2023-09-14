import datetime
import unittest
from flask import Flask
from flask_testing import TestCase
from data import app, db, User, Car, FormData, Booking

class MyTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_model(self):
        user = User(email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        assert User.query.count() == 1

    def test_car_model(self):
        car = Car(make='make', model='model', year=2023, condition='new', color='red', price='10000', PlateNo='123')
        db.session.add(car)
        db.session.commit()
        assert Car.query.count() == 1

    def test_form_data_model(self):
        form_data = FormData(fname='fname', mname='mname', lname='lname', phone='phone', email='email', PlateNo='123')
        db.session.add(form_data)
        db.session.commit()
        assert FormData.query.count() == 1

    def test_booking_model(self):
        booking = Booking(pickup_date=datetime.date.today(), pickup_location='location', dropoff_date=datetime.date.today(), dropoff_location='location', vehicle_type='type')
        db.session.add(booking)
        db.session.commit()
        assert Booking.query.count() == 1

if __name__ == '__main__':
    unittest.main()
