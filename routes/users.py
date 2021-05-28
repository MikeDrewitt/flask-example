from datetime import datetime
from flask import Blueprint, request

from constants.status import Ok, Created, NotFound, Deleted, BadRequest
from validators.users import Validate

from database import db
from models.users import Users


users_router = Blueprint('users_router', __name__)


@users_router.route('/users/', methods=['GET'])
def get_list():
    results = Users.query.all()
    users = [user.serialize() for user in results]

    return Ok(users)


@users_router.route('/users/<int:id>', methods=['GET'])
def retrieve(id):
    user = Users.query.get(id)

    if (user == None):
        return NotFound('Unable to find user')

    return Ok(user.serialize())


@users_router.route('/users/', methods=['POST'])
def create():
    valid = Validate(request.json)

    if not valid:
        return BadRequest()

    username = request.json['username']
    name = request.json['name']
    email = request.json['email']

    new_user = Users(username, name, email)

    db.session.add(new_user)
    db.session.commit()

    return Created(new_user.serialize())


@users_router.route('/users/<int:id>', methods=['PUT'])
def update(id):
    valid = Validate(request.json)

    if not valid:
        return BadRequest()

    user = Users.query.get(id)

    if (user == None):
        return NotFound('Unable to find user')

    username = request.json['username']
    name = request.json['name']
    email = request.json['email']

    user.username = username
    user.name = name
    user.email = email

    db.session.commit()

    return Ok(user)


@users_router.route('/users/<int:id>', methods=['DELETE'])
def delete(id):
    user = Users.query.get(id)

    if (user == None):
        return NotFound('Unable to find user')

    user.deleted_at = datetime.utcnow()

    db.session.commit()

    return Deleted()
