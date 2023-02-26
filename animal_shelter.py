from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient("mongodb://%s:%s@localhost:56017/?authMechanism=DEFAULT&authSource=AAC" % (username, password))
        self.database = self.client['AAC']

# C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            print("No data parameter!")
            return False

# R in CRUD
    def read_all(self, data):
        return self.database.animals.find(data, {'_id':False})
    
    def read(self, data):
        return self.database.animals.find_one(data)
    
# U in CRUD
    def update_all(self, filter_map, update):
        return self.database.animals.update_many(filter_map, update).raw_result
    
    def update(self, filter_map, update):
        return self.database.animals.update_one(filter_map, update).raw_result
    
# D in CRUD
    def delete_all(self, data):
        return self.database.animals.delete_many(data).raw_result

    def delete(self, data):
        return self.database.animals.delete_one(data).raw_result