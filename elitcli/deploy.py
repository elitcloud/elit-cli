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

__author__ = "Gary Lai"

import sys
import errno
import os
from elitcli.config import *


class Deployment(object):

    def __init__(self, credential):
        self.cwd = os.getcwd()
        self.credential = credential

    def valid_project(self):
        try:
            if not os.path.isfile(APP_ENTRY):
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), APP_ENTRY)
        except FileNotFoundError as e:
            print(e)
            sys.exit(e.errno)

        sys.path.append(self.cwd)
        try:
            import app
        except ModuleNotFoundError as e:
            print(e)
            sys.exit()
        except ImportError as e:
            print(e)
            sys.exit()
        finally:
            sys.path.remove(self.cwd)

        for func in APP_ATTR:
            try:
                getattr(app, func)
            except AttributeError as e:
                print(e)
                sys.exit()

    def deploy(self):
        self.valid_project()
