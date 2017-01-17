from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/')
def homepage():
    return render_template('Homepage.html')

@app.route('/Python')
def python():
    return render_template('Python.html')

@app.route('/python/pythonbasics')
def pythonbasics():
    return render_template('pythonbasics.html')

@app.route('/python/pyvariables')
def pyvariables():
    return render_template('pyvariables.html')

@app.route('/python/pyfunctions')
def pyfunctions():
    return render_template('pyfunctions.html')

@app.route('/python/pyselection')
def pyselection():
    return render_template('pyselection.html')

@app.route('/python/pyiteration')
def pyiteration():
    return render_template('pyiteration.html')

@app.route('/python/pylists')
def pylists():
    return render_template('pylists.html')

@app.route('/SQL')
def SQL():
    return render_template('SQL.html')

@app.route('/SQL/sqlSyntax')
def sqlSyntax():
    return render_template('sqlSyntax.html')

@app.route('/SQL/sqlSelect')
def sqlSelect():
    return render_template('sqlSelect.html')

@app.route('/SQL/sqlUpdate')
def sqlUpdate():
    return render_template('sqlUpdate.html')

@app.route('/SQL/sqlInsert')
def sqlInsert():
    return render_template('sqlInsert.html')

@app.route('/SQL/sqlCreate')
def sqlCreate():
    return render_template('sqlCreate.html')

@app.route('/SQL/sqlRelations')
def sqlRelations():
    return render_template('sqlRelations.html')

@app.route('/HTML')
def html():
    title='HTML & CSS Introduction'
    return render_template('html_INTRO.html', pagetitle=title)

@app.route('/CSS-Content')
def csscontent():
    title= 'CSS CONTENT'
    return render_template('html_css_content.html', pagetitle=title)

@app.route('/Git')
def git():
    return render_template('Git.html', pagetitle='Git Content')

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
