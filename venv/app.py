from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        first_name = request.form['first_name']
        surname = request.form['surname']
        email = request.form['email']
        message = request.form['message']

        # Create a new Contact instance and add it to the database
        contact = Contact(first_name=first_name, surname=surname, email=email, message=message)
        db.session.add(contact)
        db.session.commit()

        # Redirect back to the home page (index.html)
        return render_template('index.html', js_link="script.js")

if __name__ == '__main__':
    app.run(debug=True)
