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

import fire
from elitcli.utils import valid_boilerplate_name


class ElitCli(object):

    def new(self, name):
        """
        Create a boilerplate for training. "elit new myapp" creates a
        new boilerplate in ./myapp.
        :param name: name of boilerplate
        """
        boilerplate_name = valid_boilerplate_name(name)


if __name__ == '__main__':
    fire.Fire()