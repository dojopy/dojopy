import os
import json


class SimpleDB(object):
    def __init__(self, path_db):
        self.db = {}
        self.path_db = os.path.abspath(path_db)
        self.load(self.path_db)

    def load(self, path_db):
        if os.path.exists(path_db):
            with open(self.path_db) as file:
                self.db = json.load(file)

    def dumpdb(self):
        try:
            with open(self.path_db, 'w+') as file:
                json.dump(self.db, file)
            return True
        except Exception as e:
            print(str(e))
            return False

    def set(self, key, value):
        self.db[str(key)] = value
        return self.dumpdb()

    def get(self, key):
        try:
            return self.db[key]
        except Exception as e:
            print('not value found %s' % str(key))
            return False

    def delete(self, key):
        if not (key in self.db):
            return False
        del self.db[key]
        return self.dumpdb()

    def get_all(self):
        return json.dumps(self.db, indent=4, sort_keys=True)

    def resetdb(self):
        self.db = {}
        return self.dumpdb()


# db = SimpleDB('./db.json')
# db.set('name', 'Elon Musk')
# db.set('company', 'Space X')
# db.set('age', '48')
# db.get('name')
# print(db.get_all())
# db.delete('name')
# print(db.get_all())
# db.resetdb()
# print(db.get_all())
