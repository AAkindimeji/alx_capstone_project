from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Contact  # Import the Contact class

app = Flask(__name__)

# Database configuration (replace with your details)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://learnakins:Akins@1234@127.0.0.1/contact'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')  # Render the index template

@app.route('/submit_form', methods=['POST'])  # Define route and methods
def submit_form():
    # Get data from the form
    first_name = request.form.get('first-name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    message = request.form.get('message')

    # Create a Contact object
    contact = Contact(first_name=first_name, surname=surname, email=email, message=message)

    # Add the contact to the database session
    db.session.add(contact)

    # Save changes to the database
    db.session.commit()

    # Render the index template with a success flag
    return render_template('index.html', submitted=True)

if __name__ == '__main__':
    db.create_all()  # Create database tables if they don't exist (optional)
    app.run(debug=True)
