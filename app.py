from flask import Flask, url_for, render_template
from markupsafe import escape
from flask import request
from picamera import PiCamera
from time import sleep

app = Flask(__name__)
camera = PiCamera()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livefeed')
def livefeed():
    return render_template('livefeed.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

#-------------------------------------------------------------

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile' .format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Helena'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
