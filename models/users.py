#!/bin/python


import json


class User():


    def __init__(self, _id, name, email):
        self.set_id(_id)
        self.set_name(name)
        self.set_email(email)


    def get_id(self):
        return self._id


    def set_id(self, _id):
        self.validate_id(_id)
        self._id = _id


    def get_name(self):
        return self.name


    def set_name(self, name):
        self.validate_name(name)
        self.name = name


    def get_email(self):
        return self.email


    def set_email(self, email):
        self.validate_email(email)
        self.email = email


    @staticmethod
    def validate_id(value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError


    @staticmethod
    def validate_name(value):
        if not isinstance(value, str):
            raise TypeError(type(value))
        if not value:
            raise ValueError


    @staticmethod
    def validate_email(value):
        if not isinstance(value, str):
            raise TypeError
        if not value:
            raise ValueError


    @staticmethod
    def from_json_string(value):
        obj = json.loads(value, 'utf-8')
        if not '_id' in obj:
            raise ValueError
        if not 'name' in obj:
            raise ValueError
        if not 'email' in obj:
            raise ValueError
        _id = obj['_id']
        name = obj['name']
        email = obj['email']
        return User(_id, name, email)


    def to_json_object(self):
        return {
            '_id': self._id,
            'name': self.name,
            'email': self.email,
        }
