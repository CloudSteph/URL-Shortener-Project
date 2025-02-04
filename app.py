# Importing Flask
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)


# Define a route for the homepage "/"
@app.route('/')
def home():
    return "Welcome to the URL Shortener!"


# Run the app when the script is executed
if __name__ == '__main__':
    app.run(debug=True)
