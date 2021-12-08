from flask import (
    Blueprint
)

bp = Blueprint('blueprint', 'blueprint', url_prefix='/blueprint')


@bp.route("/example", methods=('GET', ))
def blueprint_example():
    return "<p>Hello from the blueprint!</p>"
