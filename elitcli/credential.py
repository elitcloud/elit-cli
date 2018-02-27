# ========================================================================
# Copyright 2018 Emory University
#
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
# ========================================================================
import sys
import json
from collections import namedtuple
from elitcli.config import *

__author__ = "Gary Lai"

ReadOnlyCredentials = namedtuple('ReadOnlyCredentials', ['api_key'])


class Credential(object):

    def __init__(self):
        self.api_key = self._api_key

    @staticmethod
    def load_credential_file():
        try:
            with open(CONFIG_FILE, 'r') as f:
                return f
        except FileNotFoundError as e:
            print(e)
            print('Please use \'elit configure\' to set up credential. ')
            sys.exit()

    @staticmethod
    def load_credential(f):
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print('Loading {config} has failed. '.format(config=CONFIG_FILE))
            print('Please use \'elit configure\' to set up credential. ')
            sys.exit()

    @property
    def _api_key(self):
        d = json.load(self.load_credential(self.load_credential_file()))
        try:
            return ReadOnlyCredentials(d[API_KEY])
        except KeyError as e:
            print('Missing key: \'{e}\' '.format(e=e))
            sys.exit()
