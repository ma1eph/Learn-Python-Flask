#!/bin/python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from models.users import User


class UsersTest(unittest.TestCase):


    def test_get_methods(self):
        u = User(0, 'NAME', 'EMAIL')
        self.assertEquals(0, u.get_id())
        self.assertEquals('NAME', u.get_name())
        self.assertEquals('EMAIL', u.get_email())

        with self.assertRaises(TypeError):
            User('0', 'NAME', 'EMAIL')

        with self.assertRaises(ValueError):
            User(-1, 'NAME', 'EMAIL')

        with self.assertRaises(TypeError):
            User(0, None, 'EMAIL')

        with self.assertRaises(ValueError):
            User(0, '', 'EMAIL')

        with self.assertRaises(TypeError):
            User(0, 'NAME', None)

        with self.assertRaises(ValueError):
            User(0, 'NAME', '')


    def test_set_methods(self):
        u = User(0, 'NAME', 'EMAIL')
        u.set_id(1)
        self.assertEquals(1, u.get_id())
        u.set_name('BETA')
        self.assertEquals('BETA', u.get_name())
        u.set_email('CHARLIE')
        self.assertEquals('CHARLIE', u.get_email())

        with self.assertRaises(TypeError):
            u.set_id('0')

        with self.assertRaises(ValueError):
            u.set_id(-1)

        with self.assertRaises(TypeError):
            u.set_name(None)

        with self.assertRaises(ValueError):
            u.set_name('')

        with self.assertRaises(TypeError):
            u.set_email(None)

        with self.assertRaises(ValueError):
            u.set_email('')


    def test_from_json_string(self):
        s = '{"_id":0,"name":"NAME","email":"EMAIL"}'
        u = User.from_json_string(s)
        self.assertEquals(0, u.get_id())
        self.assertEquals('NAME', u.get_name())
        self.assertEquals('EMAIL', u.get_email())


    def test_to_json_object(self):
        u = User(0, 'NAME', 'EMAIL')
        obj = u.to_json_object()
        self.assertIn('_id', obj)
        self.assertEquals(0, obj['_id'])
        self.assertIn('name', obj)
        self.assertEquals('NAME', obj['name'])
        self.assertIn('email', obj)
        self.assertEquals('EMAIL', obj['email'])


if __name__ == '__main__':
    unittest.main()
