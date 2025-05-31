from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = '********'  # Use environment variable in production

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '*****'
app.config['MYSQL_DB'] = 'romio'

mysql = MySQL(app)

# ---------------------------
# ROUTES
# ---------------------------

@app.route('/')
def index():
    return redirect('/login')

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("User already exists. Please log in.", "error")
        else:
            hashed_pw = generate_password_hash(password)
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_pw))
            mysql.connection.commit()
            flash("Signup successful! Please log in.", "success")
            cursor.close()
            return redirect('/login')

        cursor.close()
    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password_input = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[2], password_input):
            session['user_email'] = email
            flash("Login successful!", "success")
            return redirect('/dashboard')
        else:
            flash("Invalid email or password.", "error")

    return render_template('login.html')

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        flash("Please log in to continue.", "error")
        return redirect('/login')

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, title, location, date FROM trips WHERE user_email = %s", (session['user_email'],))
    trips = cursor.fetchall()
    cursor.close()
    return render_template('dashboard.html', trips=trips)

# Trip Detail Route
@app.route('/trip/<int:trip_id>')
def trip_detail(trip_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM trips WHERE id = %s", (trip_id,))
    trip = cursor.fetchone()
    cursor.close()
    return render_template('trip_detail.html', trip=trip)

# Review Route
@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        email = session.get('user_email')
        review_text = request.form['review_text']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO reviews (user_email, review, created_at) VALUES (%s, %s, %s)",
                       (email, review_text, datetime.now()))
        mysql.connection.commit()
        cursor.close()
        flash("Thank you for your review!", "success")
        return redirect('/dashboard')

    return render_template('review.html')

# Memories Route
@app.route('/memories')
def memories():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM memories WHERE user_email = %s", (session['user_email'],))
    memories = cursor.fetchall()
    cursor.close()
    return render_template('memories.html', memories=memories)

# Profile Route
@app.route('/profile')
def profile():
    email = session.get('user_email')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM trips WHERE user_email = %s", (email,))
    trip_count = cursor.fetchone()[0]
    cursor.close()
    return render_template('profile.html', user={
        'email': user[1],
        'created_at': user[3],
        'trip_count': trip_count
    })

# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect('/login')

# ---------------------------
# Run the App
# ---------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
