from flask import Flask, url_for, render_template # To access .html templates 
from markupsafe import escape
from flask import request # To utilize HTML method for accessing URL
from time import sleep

app = Flask(__name__) # Start of application

@app.route('/') # Home page
def index():
    return 'index.html'

@app.route('/livefeed') # Routing to Livefeed window
def livefeed():
    return render_template('livefeed.html')

@app.route('/statistics') # Routing to Statistics window
def statistics():
    return render_template('statistics.html')

@app.route('/login', methods=['GET', 'POST'])  # HTML method for accessing URL
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':          # End of application
    app.run(debug=True, host='localhost')
