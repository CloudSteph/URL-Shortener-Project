# Import necessary modules
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string

# Create a Flask app instance
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)


# Define URL model for database
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_code = db.Column(db.String(8), unique=True, nullable=False)
    long_url = db.Column(db.String(2500), nullable=False)


# Generate a random short code
def generate_short_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# Define a route for the homepage to handle URL shortening  "/"
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']  # Get user input from form

        # Generate a unique short code
        short_code = generate_short_code()  # Generate a short code
        while URL.query.filter_by(short_code=short_code).first():
            short_code = generate_short_code()

        # Save the new URL mapping to the database
        new_url = URL(short_code=short_code, long_url=long_url)
        db.session.add(new_url)
        db.session.commit()

        # Construct the full short URL to display
        short_url = request.host_url + short_code
        return render_template("index.html", short_url=short_url)

    # Display form without a short URL
    return render_template("index.html", short_url=None)


# Route to handle redirection from short URL to the original long URL
@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()  # Look up the short code
    if url_entry:
        return redirect(url_entry.long_url)  # Redirect to the original URL
    return "URL not found", 404  # Show error if code doesn't exist


# Run the Flask app when the script is executed and create database tables if they don't exist
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
