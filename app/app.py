from flask import Flask, url_for, redirect, request, Markup, render_template, session, flash
import json, datetime

app = Flask(__name__)
app.config.from_object('app.config')

# DISABLE DEBUG FOR PRODUCTION!
app.debug = False


def clear_session():
    session['last_action'] = None
    # using session.clear() nulls everything, including the session itself, so you have to check for session AND session['key'] or pop(None) individual session keys
    # session.clear()


# Check credentials, modify session, etc.
@app.before_request
def before_request():
    if 'session_start' not in session:
        session['session_start'] = datetime.datetime.now()
    session['last_action'] = datetime.datetime.now()


@app.route('/index')
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/search', methods=['GET'])
def search():
    searchword = request.args.get('query', '')
    if searchword == '':
        flash('No query value was provided.')
    return render_template('search.html', query_return=searchword)


@app.route('/logout')
def logout():
    clear_session()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error_info='404: Page not found')


@app.errorhandler(413)
def not_found(error):
    return render_template('error.html', error_info='413: Upload size exceeded')


@app.errorhandler(500)
def internal_server_error(error):
    # This may pass system errors you do not wish users to see
    return render_template('error.html', error_info=error.args)


# What version of python is active?
# import sys
# @app.route('/pyversion')
# def pyversion():
#     return sys.version
