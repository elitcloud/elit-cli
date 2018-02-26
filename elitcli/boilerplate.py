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

import os
import string
import unicodedata
import errno
from elitcli import templates
from distutils.dir_util import copy_tree

__author__ = "Gary Lai"


class Boilerplate(object):

    def __init__(self, name):
        self.name = self.valid_boilerplate_name(name)
        self.template_path = os.path.dirname(templates.__file__)

    @staticmethod
    def valid_boilerplate_name(name, replace=' '):
        """
        Convert name from user into a valid python package name
        :param name: :param name: boilerplate name
        :param replace: \' \'
        :return: boilerplate name
        """

        valid_filename_chars = "_%s" % string.ascii_letters

        for r in replace:
            name = name.replace(r, '_')

        name = "_".join(name.split("_"))

        cleaned_filename = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode()
        cleaned_filename = ''.join(c for c in cleaned_filename if c in valid_filename_chars).lower()

        return "_".join(list(filter(None, cleaned_filename.split("_"))))

    def build(self):
        cwd = os.getcwd()
        os.chdir(cwd)
        try:
            os.makedirs(self.name)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            else:
                print('\"{name}\" exists in current directory'.format(name=self.name))
        dest = "{cwd}/{name}".format(cwd=cwd, name=self.name)
        copy_tree(self.template_path, dest)