# Import neccessary modules
from flask import Flask, request
import random
import string

# Create a Flask app instance
app = Flask(__name__)

# Dictionary to temporarily store short and long URLs
url_db = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Define a route for the homepage "/"
@app.route('/', methods=['GET', 'POST'])
def home