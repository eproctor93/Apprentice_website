from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/layout')
def layout():
    return render_template('layout.html', pagetitle='LAYOUT')

@app.route('/')
def homepage():
    return render_template('Homepage.html', pagetitle='IT Solutions Apprenticeship')

@app.route('/Python')
def python():
    return render_template('Python.html', pagetitle='Python')

@app.route('/SQL')
def SQL():
    return render_template('SQL.html', pagetitle='SQL')

@app.route('/HTML')
def html():
    title='HTML & CSS Introduction'
    return render_template('HTML-CSS.html', pagetitle=title)

@app.route('/Git')
def git():
    return render_template('Git.html', pagetitle='Git Content')

@app.route('/Java')
def java():
     return render_template('Java.html', pagetitle='Java')

@app.route('/Personal-Experiences')
def personalexperiences():
    return render_template('PE.html', pagetitle='Personal Experiences')

@app.route('/Links')
def links():
    return render_template('Links.html', pagetitle='Useful Links')

if __name__ == "__main__":
    app.run(debug=True)
