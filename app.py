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
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        url_db[short_code] = long_url
        short_url = request.host_url + short_code
        return f'Welcome to the URL Shortener!"<br>Shortened URL: <a href="{short_url}">{short_url}</a>'

    # Display form with welcome message
    return '''
        <h1>Welcome to the URL Shortener!</h1>
        <form method="post">
            Enter URL: <input type="text" name="long_url">
            <input type="submit" value="Shorten">
        </form>
    '''


# Run the Flask app when the script is executed
if __name__ == '__main__':
    app.run(debug=True)
