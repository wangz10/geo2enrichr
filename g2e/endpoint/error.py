"""Error handling.

__authors__ = "Gregory Gundersen"
__credits__ = "Ma'ayan Lab, Icahn School of Medicine at Mount Sinai"
__contact__ = "avi.maayan@mssm.edu"
"""


from flask import Blueprint
from g2e.app.config import BASE_URL
from g2e.app import app
from flask import render_template


error = Blueprint('error', __name__, url_prefix=BASE_URL)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')