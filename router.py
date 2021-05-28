from flask import Blueprint

from routes.status import status_router
from routes.users import users_router

router = Blueprint('router', __name__)

router.register_blueprint(status_router)
router.register_blueprint(users_router)
