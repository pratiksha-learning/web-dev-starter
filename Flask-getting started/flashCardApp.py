from flask import Flask, render_template

app = Flask(__name__)

# print(__name__) -> __main__
# print(app) -> <Flask 'flashCardApp'>

# view function:
@app.route('/')
def Welcome():
    return "Welcome to my flash card application"


# Model-Template-View pattern
@app.route('/mtv')
def MTV():
    '''
    Model Template View pattern is a pattern which renders html templates
    with render_template method. We can pass variables we want to show in html 
    created in templates folder with {{variable_name}} -> Jinja variable

    Templates should be stored in "templates" folder only as the name written
    '''
    return render_template("MyTemplate.html", message="This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.")