from flask import render_template, redirect, url_for, flash, request, current_app
# from flask_login import current_user
from app.main import bp

##############################################################################
# Main blueprint
##############################################################################


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')
