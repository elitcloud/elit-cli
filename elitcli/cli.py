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
"""
Usage:
    elit configure
    elit new <name>
    elit deploy
    elit (-h | --help | --version)

Options:
    -h --help       Show this screen.
    --version       Show version.

Description:
    elitcli is used for accessing resources to ELIT cloud.

See 'elit help <command>' for more information on a specific command.
"""
import os

__author__ = "Gary Lai"

from docopt import docopt
from elitcli.version import version
from elitcli.credential import Credential
from elitcli.boilerplate import Boilerplate
from elitcli.deploy import Deployment


def main():
    args = docopt(__doc__, version=version)
    credential = Credential()
    if args['new']:
        boilerplate_name = args['<name>']
        boilerplate = Boilerplate(boilerplate_name)
        boilerplate.build()
    elif args['configure']:
        credential.setup()
    elif args['deploy']:
        deployment = Deployment(credential)
        os.chdir(deployment.cwd)
        deployment.deploy()


if __name__ == '__main__':
    main()
