from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"

users = {
    "admin": generate_password_hash("admin101"),
    "rokon": generate_password_hash("rokon123"),
    "tawhide": generate_password_hash("tawhide234"),
    "sahosh": generate_password_hash("sahosh345"),
    "kawsar": generate_password_hash("kawsar456"),
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and check_password_hash(users[username], password):
        flash('Logged in successfully!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Invalid username or password', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
