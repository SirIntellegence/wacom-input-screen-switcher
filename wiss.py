#!/usr/bin/python3
#
# Copyright 2017 SirIntellegence <sirintellegence2@gmail.com>
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
#
#
import sys
import screeninfo
import getopt
import typing
import subprocess
import re

# from subprocess import call

# transform matrix values
#  | scale x    0           xtranslate|
#  | 0          yscale      ytranslate|
#  | 0          0           1         |


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class device:
    deviceName = ""
    id
    type

    def __init__(self, name: str, id: int, type: str):
        self.deviceName = name
        self.id = id
        self.type = type
        pass


class wiss:
    def __init__(self):

        pass

    def __usage(self):
        pass

    def moveOutput(self, argv):
        try:
            opts, args = getopt.getopt(argv, "")
        except getopt.GetoptError:
            self.__usage()
            sys.exit(2)
        devices = self.getDevices()
        if (len(devices) < 1):
            eprint("No tablet devices were found")
            sys.exit(3)

        pass

    def getDevices(self) -> list:
        tempResult = subprocess.check_output(["xsetwacom", "--list",
                                              "devices"], bufsize=100).decode("utf-8")
        matches = re.findall(r"(.+)\tid: (\d+)\ttype:\s(.+)\s*", tempResult)
        results = []
        for m in matches:
            results.append(device(m[0], int(m[1]), m[2].strip()))
        return results

    def _getCurrOutput(self, id: int) -> str:

    def _getOutputList(self) -> list:
        pattern = re.compile(r"\S+")
        # note: may return invalid results if there is more than one xscreen
        tempResult = subprocess.check_output(["xrandr"], bufsize=100).
            decode("utf-8")
        first = false
        results = []
        for line in tempResult.split('\n'):
            if first:
                first = False
                continue
            if line[0] == ' '
                continue
            results.append(pattern.search(line).group(0))

        return results

    def getMappedArea(self, device: device):
        # device.
        call()
        results = []
        pass


if (__name__ == "__main__"):
    wiss = wiss()
    wiss.moveOutput(sys.argv[1:])
