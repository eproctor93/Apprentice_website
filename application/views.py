from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/layout')
def layout():
    return render_template('layout.html', title="Layout")

@app.route('/')
def homepage():
    return render_template('Homepage.html', title="Homepage")

@app.route('/Python')
def python():
    return render_template('Python.html', title="Python")

@app.route('/SQL')
def SQL():
    return render_template('SQL.html', title="SQL")

@app.route('/HTML')
def html():
    return render_template('html_css_page_INTRO.html', title="HTML & CSS")

@app.route('/HTML-Content')
def htmlcontent():
    return render_template('html_css_page_html_content.html', title="HTML-Content")

@app.route('/HTML-CSS')
def htmlcss():
    return render_template('html_css_page_css_content.html', title="HTML-CSS-Content")

@app.route('/Git')
def git():
    return render_template('Git.html', title="Git")

@app.route('/Java')
def java():
    return render_template('Java.html', title="Java")

@app.route('/Personal-Experiences')
def personalexperiences():
    return render_template('PE.html', title="Personal Experiences")

@app.route('/Links')
def links():
    return render_template('Links.html', title="Useful Links")

if __name__ == "__main__":
    app.run()
