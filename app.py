from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql.cursors
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Database connection
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="PASSWORD",  # Replace with your DB password
        database="bank_management",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['username']
    contact_no = request.form['contact_no']
    amount = float(request.form['amount'])
    city = request.form['city']
    state = request.form['state']

    if amount < 1000:
        flash("Minimum amount must be ₹1000.")
        return redirect(url_for('index'))

    account_number = str(random.randint(1000000000, 9999999999))
    query = """
    INSERT INTO customers (account_number, username, contact_no, amount, city, state) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (account_number, username, contact_no, amount, city, state)
    
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
            flash(f"Account created! Your Account Number: {account_number}")
    except Exception as e:
        flash(f"Error creating account: {e}")
    finally:
        connection.close()
    
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    account_number = request.form['account_number']

    query = "SELECT * FROM customers WHERE username=%s AND account_number=%s"

    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(query, (username, account_number))
            user = cursor.fetchone()
            if user:
                return render_template('dashboard.html', user=user)
            else:
                flash("Account not found!")
    except Exception as e:
        flash(f"Error during login: {e}")
    finally:
        connection.close()
    
    return redirect(url_for('index'))

@app.route('/credit', methods=['POST'])
def credit_amount():
    account_number = request.form['account_number']
    amount = float(request.form['amount'])

    query = "UPDATE customers SET amount = amount + %s WHERE account_number=%s"
    
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(query, (amount, account_number))
            connection.commit()
            flash(f"₹{amount} credited successfully!")
    except Exception as e:
        flash(f"Error during credit: {e}")
    finally:
        connection.close()

    return redirect(url_for('index'))

@app.route('/debit', methods=['POST'])
def debit_amount():
    account_number = request.form['account_number']
    amount = float(request.form['amount'])

    query_balance = "SELECT amount FROM customers WHERE account_number=%s"
    query_debit = "UPDATE customers SET amount = amount - %s WHERE account_number=%s"

    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(query_balance, (account_number,))
            balance = cursor.fetchone()['amount']

            if amount <= balance:
                cursor.execute(query_debit, (amount, account_number))
                connection.commit()
                flash(f"₹{amount} debited successfully!")
            else:
                flash("Insufficient balance!")
    except Exception as e:
        flash(f"Error during debit: {e}")
    finally:
        connection.close()

    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_account():
    account_number = request.form['account_number']
    query = "DELETE FROM customers WHERE account_number=%s"

    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(query, (account_number,))
            connection.commit()
            flash("Account deleted successfully!")
    except Exception as e:
        flash(f"Error deleting account: {e}")
    finally:
        connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)





