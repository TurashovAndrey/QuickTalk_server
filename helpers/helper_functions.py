import simplejson

def get_json_argument(self, name, default=[]):
    try:
        args = simplejson.loads(unicode(self.request.body, 'utf-8'))

        if not name in args.keys():
            return unicode(default)
        return args[name]
    except:
        return None

