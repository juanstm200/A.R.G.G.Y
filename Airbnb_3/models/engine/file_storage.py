#!/usr/bin/python3
"""
Here, the class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os.path

class FileStorage():
    """ Initialization of class attributes """

    __file_path = "objects_info.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj """

        """ Find the name of the key for the dictionary __objects """
        key = obj.__class__.__name__ + "." + obj.id

        """ Update the dictionary __objects with the new object """
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """

        obj_dict = {}
        for key, obj in self.all().items():
            """ Each object dictionary is saved for later serialization """
            if type(obj) is dict:
                obj_dict[key] = obj
            else:
                obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode="w") as open_file:
            """ Here the dictionary obj_dict is serializated and is saved """
            json.dump(obj_dict, open_file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        """ Verify if the file exists """
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, mode="r", encoding='UTF-8') as open_file:
                    dict_objs = json.load(open_file)
                    for key, value in dict_objs.items():
                        self.new(BaseModel(**value))
        except:
            pass

    def find_key(self, key):
        from models.base_model import BaseModel
        """ Find if a key exists in the __object dictionaty """
        if key in self.all():
            obj = self.all().get(key)
            obj = obj.to_dict()
            return BaseModel(**obj)
        else:
            return None
