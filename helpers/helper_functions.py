import simplejson
import uuid


def get_json_argument(jsonbody, name, default=[]):
    try:
        args = simplejson.loads(unicode(jsonbody, 'utf-8'))

        if not name in args.keys():
            return unicode(default)
        return args[name]
    except:
        return None


def verify_uuid(val):
    if not isinstance(val, uuid.UUID):
        try:
            val = uuid.UUID(val)
        except ValueError, e:
            raise ValueError(e)
    return val

