from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # Process the registration form data
        name = request.form['name']
        email = request.form['email']
        
        # Perform necessary operations with the form data (e.g., saving to a database)
        
        # Redirect to a success page or return a success message
        
    return render_template('registration.html')

@app.route('/amendments')
def amendments():
    # Handle amendments logic
    return render_template('amendments.html')

@app.route('/appeals')
def appeals():
    # Handle appeals logic
    return render_template('appeals.html')

@app.route('/annual_returns')
def annual_returns():
    # Handle annual returns logic
    return render_template('annual_returns.html')

if __name__ == '__main__':
    app.run(debug=True)
