from datetime import datetime
from dateutil import parser

def json_dumps_handler(obj):
  if isinstance(obj, datetime):
    return obj.isoformat() + 'Z'
  elif hasattr(obj, 'isoformat'):
    return obj.isoformat()
  #elif isinstance(obj, ...):
  #  return ...
  else:
    raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj))

def kwargs_converter(kwargs):
  return {key:param_converter(val) for key, val in kwargs.items() if val is not None}

def param_converter(obj):
  if isinstance(obj, datetime):
    return obj.isoformat() + 'Z'
  elif hasattr(obj, 'isoformat'):
    return obj.isoformat()
  elif obj is True:
    return 'true'
  elif obj is False:
    return 'false'
  else:
    return obj


def response_converter(json):
  if isinstance(json, dict):
    for key, val in json.iteritems():
      if isinstance(val, dict):
        json[key] = response_converter(val)
      elif isinstance(val, list):
        json[key] = [response_converter(item) for item in val]
      elif isinstance(val, basestring):
        if key.endswith('_at'):
          try:
            json[key] = parser.parse(json[key], ignoretz=True)
          except Exception, e:
            continue
  return json