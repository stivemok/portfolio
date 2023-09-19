
# Easy Car Rental Website
![homepage](https://github.com/stivemok/portfolio/assets/46189207/06dfb94a-a5fa-4869-a124-ecbbfb3abe4b)
Welcome to the Easy Car Rental website! Our website offers a simple and convenient way to book rental cars, register your car for rental, and manage your account through our admin login. Here’s a brief overview of our main features:

# Booking
Our booking system is designed to make it easy for you to find and reserve the perfect car for your needs. Simply enter your desired pick-up and drop-off dates and locations, and we’ll show you a selection of available cars to choose from. You can filter the results by car type, price, and other features to find the perfect match.


# Car Registration
If you own a car that you’d like to rent out through our platform, you can easily register it on our website. Simply provide some basic information about your car, such as its make, model, year, and location, and we’ll take care of the rest. You’ll be able to manage your car’s availability and rental rates through our admin login.

# Admin Login
Our admin login allows you to manage your account and rental activity on our website. You can view your upcoming reservations, update your personal information, and manage your car’s availability and rental rates if you’ve registered it on our platform.

# About Page
If you’d like to learn more about our company and our mission, please visit our About page. We’re dedicated to providing a simple and convenient car rental experience for our customers. 

# Flask Web Application and Unit Testing
This project is a Flask web application that includes SQLAlchemy models for a car rental service. The application includes routes for handling user registration, vehicle information retrieval, vehicle booking, and form submission. The application also includes unit tests to ensure the functionality of the application.

# Getting Started
## Install Prerequisites
To deploy this project run

```bash
  pip install -r requirements.txt
```

# Prerequisites
1. Python 3
2. pip
3. Flask
4. Flask-SQLAlchemy
5. Flask-Testing

# Running the Application
Save the Flask application code to a Python file, for example data.py.
Set up your database. The code is currently configured to use a MySQL database. Replace 'mysql://root:stivemok@localhost/easy' with your own MySQL URI.
Run the application using Python:
```bash
  python3 data.py
```
python3 data.py or if you include python3 header you can use ./data.py

This will start a server on localhost at port 5000. You can access it by going to http://localhost:5000/easy in your web browser.

# Running the Tests

1. Save the testing code to a separate Python file, for example test_data.py
2. Run the tests using unittest:
```bash
  python3 -m unittest test_data.py
```

# Application Structure
The application includes several SQLAlchemy models:

1. User: Represents a user in the system.
2. Car: Represents a car available for rent.
3. FormData: Represents form data submitted by users.
4. Booking: Represents a vehicle booking.

# The application also includes several routes:

1. /admin, /VehicelRegistration, /about, etc.: Render different pages of the website.
2. /login, /register, etc.: Handle user authentication and registration.
3. /submit-form, /submit_car, etc.: Handle form submissions and add new objects to the database.
4. /get-vehicle-info, /book-vehicle, etc.: Retrieve data from the database and return it in a JSON response.


