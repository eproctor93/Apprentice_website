from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/Homepage')
def homepage():
    return render_template('Homepage.html')

@app.route('/Python')
def python():
    return render_template('Python.html')

@app.route('/SQL')
def SQL():
    return render_template('SQL.html')

@app.route('/HTML')
def html():
    return render_template('html_css_page_INTRO.html')

@app.route('/HTML-Content')
def htmlcontent():
    return render_template('html_css_page_html_content.html')

@app.route('/HTML-CSS')
def htmlcss():
    return render_template('html_css_page_css_content.html')

@app.route('/Git')
def git():
    return render_template('Git.html')

@app.route('/Java')
def java():
    return render_template('Java.html')

@app.route('/Personal-Experiences')
def personalexperiences():
    return render_template('PE.html')

@app.route('/Links')
def links():
    return render_template('Links.html')

if __name__ == "__main__":
    app.run()
