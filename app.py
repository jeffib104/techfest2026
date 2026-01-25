from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/events')
def events():
    return render_template('events.html')
@app.route('/help')
def help():
    c_email = os.environ.get('COORD_EMAIL', 'contact@techfest26.com')
    c_phone = os.environ.get('COORD_PHONE', 'Phone number')
    c_phone1 = os.environ.get('COORD_PHONE1', 'Phone number 1')

    return render_template('help.html', coord_email=c_email, coord_phone=c_phone, coord_phone1=c_phone1)

if __name__ == '__main__':
    app.run(debug=True)