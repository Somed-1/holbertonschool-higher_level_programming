#!/usr/bin/python3
"""This module contains class Base"""
import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ method of class Base
        """
        if id is None:
            self.increase_nb()
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        
        unified_dicts = []
        for d in list_dictionaries:
            unified_dict = {'id': d['id']}  # Always include 'id' key
            if 'width' in d:
                unified_dict['width'] = d['width']
            if 'height' in d:
                unified_dict['height'] = d['height']
            if 'x' in d:
                unified_dict['x'] = d['x']
            if 'y' in d:
                unified_dict['y'] = d['y']
            if 'size' in d:
                unified_dict['size'] = d['size']
            if 'name' in d:
                unified_dict['name'] = d['name']
            unified_dicts.append(unified_dict)
        
        return json.dumps(unified_dicts)

    @classmethod
    def increase_nb(cls):
        cls.__nb_objects += 1
