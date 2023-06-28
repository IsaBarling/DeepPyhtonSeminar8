import hashlib
import json


class ExplorerObject:
    def __init__(self, name, parent, oType, size, h):
        self.oType = oType
        self.name = name
        self.parent = parent
        self.size = size
        self.oHash = hashlib.sha256((name + parent + oType + str(size)).encode()).hexdigest()

    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
