from flask import render_template
from . import main

# the error handles here will be invooked ONLY for the 'main' Blueprint. this allows us to focus at a specific issue
# instead of looking for the error for an error handler defined globaly.

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

