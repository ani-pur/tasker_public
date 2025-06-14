from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from logic import auth         # 'from login import' if not running locally
from logic import tasks        # ^
import secrets      



app = Flask(__name__)
app.secret_key = secrets.token_hex()  # Replace with a secure random secret in production

# LOGIN ROUTE
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        input_pass = request.form.get('password', '').strip()
        user = auth.verify_login(input_pass)
        if user:
            session['username'] = user
            # add logging here
            print("!! USER FOUND: ",user)
            return redirect(url_for('index'))
        else:
            error = "Invalid password. Please try again."
            ipAddr=request.remote_addr
            print("!! FAILED LOGIN FROM IP: ",ipAddr)
    return render_template('login.html', error=error)

# Detects if the incoming request is from a mobile device by checking the User-Agent header for common mobile keywords.
def is_mobile():        
    user_agent = request.headers.get('User-Agent', '').lower()
    mobile_keywords = ['iphone', 'android', 'mobile']
    return any(keyword in user_agent for keyword in mobile_keywords)  #bless python

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


# root route
@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Automatically choose template based on device type.
    if is_mobile():
        return render_template('mobile.html', username=session['username'])
    return render_template('desktop.html', username=session['username'])

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    if 'username' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    username = session['username']
    if request.method == 'GET':
        #idk how this works, idk why it works but get rid of it and PLEASE
        # FOR THE LOVE OF GOD, SWITCH TO A DB, IT'LL MAKE THINGS SO MUCH EASIER LOL THIS IS WASTING TIME
        tasks_list = tasks.get_all_tasks(username, 'asc')
        return jsonify(tasks_list)
    elif request.method == 'POST':
        task_data = request.get_json()
        if not task_data:
            return jsonify({'error': 'Invalid task data'}), 400
        new_task = tasks.add_task(username, task_data)
        return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 'username' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    username = session['username']
    success = tasks.delete_task(username, task_id)
    if success:
        return jsonify({'message': 'Task deleted successfully.'})
    else:
        return jsonify({'error': 'Task not found.'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')