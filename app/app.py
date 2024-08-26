from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you can handle the form data, e.g., save it to a database
        return f"Thank you, {name}! Your message has been received."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
