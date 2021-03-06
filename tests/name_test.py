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

import pytest
from elitcli.boilerplate import Boilerplate


@pytest.mark.parametrize("name, expected", [
    ("My App", "my_app"),
    ("My App!", "my_app"),
    ("!My App", "my_app"),
    ("My_App", "my_app"),
    ("My______App", "my_app"),
    (" !My    App  ", "my_app"),
    ("! My    App  ", "my_app"),
    ("!  My    App  1", "my_app"),
    ("!___  My    App  1", "my_app"),
    ("!___  My  _  App  1", "my_app"),
    ("!___  My  _  App  1", "my_app"),
])
def test_boilerplate_name(name, expected):
    assert Boilerplate(name).name == expected
