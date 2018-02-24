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

from elitcli.utils import valid_boilerplate_name


def test_boilerplate_name():
    assert valid_boilerplate_name("My App") == "my_app"
    assert valid_boilerplate_name("My App!") == "my_app"
    assert valid_boilerplate_name("!My App") == "my_app"
    assert valid_boilerplate_name("My_App") == "my_app"
    assert valid_boilerplate_name("My______App") == "my_app"
    assert valid_boilerplate_name(" !My    App  ") == "my_app"
    assert valid_boilerplate_name("! My    App  ") == "my_app"
    assert valid_boilerplate_name("!  My    App  1") == "my_app"
    assert valid_boilerplate_name("!___  My    App  1") == "my_app"
    assert valid_boilerplate_name("!___  My  _  App  1") == "my_app"