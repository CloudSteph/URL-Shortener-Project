# Import neccessary modules
from flask import Flask, request, render_template
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
def home():
    if request.method == 'POST':
        long_url = request.form['long_url'] # Get user input from form
        short_code = generate_short_code() # Generate a short code
        url_db[short_code] = long_url # Store URL in dictionary
        short_url = request.host_url + short_code # Construct short URL
        return render_template("index.html", short_url=short_url)

    # Display form with welcome message
    return render_template("index.html", short_url=None)


# Run the Flask app when the script is executed
if __name__ == '__main__':
    app.run(debug=True)
