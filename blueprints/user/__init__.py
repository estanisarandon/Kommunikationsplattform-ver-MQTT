from flask import Blueprint, render_template

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/profile')
def user_get():
    return render_template("user.html")