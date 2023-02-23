#Gregory Greene
#SNHU CS 340

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps


class AnimalShelter(object):

    def __init__(self, username, password):
        # Initializing the MongoClient 
        self.client = MongoClient('mongodb://%s:%s@localhost:30386/aac' % (username, password))
        self.database = self.client['aac']

#create method
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, data parameter empty")

#read method
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id": False})
            
        else:
            data = self.database.animals.find({},{"_id": False})
        
        return data
    
#update method
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                result = update_result.raw_result
            else:
                result = "No document found"
            return result
        else:
            raise Exception("Nothing to update, data parameter empty")

#delete method
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document found"
            return result
        else:
            raise Exception("Nothing to delete, data parameter empty")