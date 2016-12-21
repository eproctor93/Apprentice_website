from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/')
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
    title='HTML & CSS Introduction'
    return render_template('html_iNTRO.html', pagetitle=title)

@app.route('/HTML-Content')
def htmlcontent():
    title='HTML CONTENT'
    return render_template('html_html_content.html', pagetitle=title)

@app.route('/CSS-Content')
def csscontent():
    title= 'CSS CONTENT'
    return render_template('html_css_content.html', pagetitle=title)

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
