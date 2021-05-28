from flask import Blueprint

from constants.status import Ok

status_router = Blueprint('status_router', __name__)


@status_router.route('/status', methods=['GET'])
def get():
    return Ok('Hey the api is running')
