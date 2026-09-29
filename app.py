from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"
DATABASE = "database.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            type TEXT NOT NULL, -- 'Lost' or 'Found'
            category TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'Open', -- 'Open', 'Claimed', 'Resolved'
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    category = request.args.get('category', '')
    location = request.args.get('location', '')
    
    query = "SELECT * FROM items WHERE 1=1"
    params = []
    
    if category:
        query += " AND category LIKE ?"
        params.append(f"%{category}%")
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
        
    cursor.execute(query, params)
    items = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', items=items, category=category, location=location)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            flash("Registration successful! Please login.")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists!")
        finally:
            conn.close()
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials!")
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/post', methods=['GET', 'POST'])
def post_item():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        title = request.form['title']
        item_type = request.form['type']
        category = request.form['category']
        location = request.form['location']
        description = request.form['description']
        
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO items (user_id, title, type, category, location, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (session['user_id'], title, item_type, category, location, description))
        conn.commit()
        conn.close()
        
        flash("Item posted successfully!")
        return redirect(url_for('home'))
        
    return render_template('post_item.html')

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE user_id = ?", (session['user_id'],))
    user_items = cursor.fetchall()
    conn.close()
    
    return render_template('history.html', items=user_items)

@app.route('/claim/<int:item_id>')
def claim_item(item_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET status = 'Claimed' WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    
    flash("Item status updated to Claimed!")
    return redirect(url_for('history'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)