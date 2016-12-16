from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/example')
def example():
    return render_template('example.html')

if __name__ == "__main__":
    app.run()