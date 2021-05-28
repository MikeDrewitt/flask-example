from flask import jsonify


def Ok(body):
    response = jsonify(body)
    response.response_code = 200

    return response


def Created(body):
    response = jsonify(body)
    response.response_code = 201

    return response


def Deleted(message='Deleted'):
    response = jsonify({'message': message})
    response.status_code = 204

    return response


def BadRequest(message='Bad Request'):
    error = jsonify({'message': message})
    error.status_code = 400

    return error


def NotFound(message='Not Found'):
    error = jsonify({'message': message})
    error.status_code = 404

    return error
