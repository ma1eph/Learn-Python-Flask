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

import main


class MainTest(unittest.TestCase):


    def test_index(self):
        main.app.testing = True
        client = main.app.test_client()

        r = client.get('/')
        self.assertEqual(200, r.status_code)
        self.assertIn('Hello World', r.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
