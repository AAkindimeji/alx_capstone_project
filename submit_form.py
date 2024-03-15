import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    try:
        validate_email(email)
    except EmailNotValidError as e:
        return str(e), 400

    # Send email notification
    sender_email = "your_email@example.com"
    receiver_email = "your_email@example.com"
    password = "your_password"
    subject = "New message from portfolio contact form"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    return 'Form submitted successfully!', 200

if __name__ == '__main__':
    app.run(debug=True)
