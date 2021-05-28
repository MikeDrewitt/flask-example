from cerberus import Validator

schema = {
  'name': {'type': 'string', 'required': True},
  'email':{'type': 'string', 'required': True},
  'username': {'type': 'string', 'required': True},
}

def Validate(body):
  v = Validator(schema)

  return v.validate(body)
