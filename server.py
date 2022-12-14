from flask import Flask, render_template, request, redirect, url_for, session
from flask_babel import Babel, gettext, _
import os, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('menu.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator_cost.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.config.from_file('config.json', load=json.load)
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    babel = Babel(app)
    @babel.localeselector
    def get_locale():
        #return request.accept_languages.best_match(app.config['LANGUAGES'])
        return 'es'
    app.run(host='0.0.0.0', port=port, debug=True)