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
#  | x scale    0           x translate|
#  | 0          y scale     y translate|
#  | 0          0           1          |


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


class transform:
    xScale = 1
    yScale = 1
    xTranslate = 0
    yTranslate = 0

    # URL that generated this regex:
    # http://txt2re.com/index-python.php3?s=0.428571,%200.000000,%200.000000,%200.000000,%201.000000,%200.000000,%200.000000,%200.000000,%201.000000&14&-133&54&8&-134&55&9&16&61&-140&13&60&-139&12&59&-138&11&58&-137&15&57&-136&10&56&-135
    _re1 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 1
    _re2 = '(,)'  # Any Single Character 1
    _re3 = '(\\s+)'  # White Space 1
    _re4 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 2
    _re5 = '(,)'  # Any Single Character 2
    _re6 = '(\\s+)'  # White Space 2
    _re7 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 3
    _re8 = '(,)'  # Any Single Character 3
    _re9 = '(\\s+)'  # White Space 3
    _re10 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 4
    _re11 = '(,)'  # Any Single Character 4
    _re12 = '(\\s+)'  # White Space 4
    _re13 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 5
    _re14 = '(,)'  # Any Single Character 5
    _re15 = '(\\s+)'  # White Space 5
    _re16 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 6
    _re17 = '(,)'  # Any Single Character 6
    _re18 = '(\\s+)'  # White Space 6
    _re19 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 7
    _re20 = '(,)'  # Any Single Character 7
    _re21 = '(\\s+)'  # White Space 7
    _re22 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 8
    _re23 = '(,)'  # Any Single Character 8
    _re24 = '(\\s+)'  # White Space 8
    _re25 = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 9

    transformRegEx = re.compile(_re1 + _re2 + _re3 + _re4 + _re5 + _re6 + _re7 +
                                _re8 + _re9 + _re10 + _re11 + _re12 + _re13 +
                                _re14 + _re15 + _re16 + _re17 + _re18 + _re19 +
                                _re20 + _re21 + _re22 + _re23 + _re24 + _re25,
                                re.IGNORECASE | re.DOTALL)

    def parse(input: str):
        m = transformRegEx.search(input)
        xScale = int(m.group(1))
        xTranslate = int(m.group(7))
        yScale = int(m.group(13))
        yTranslate = int(m.group(16))
        pass

    # def __init__(self, transformMatch):


class screen:
    transform = transform()


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
        if (len(opts) > 0 or len(args) > 0):
            eprint("Program arguments are not supported at this time. Sorry.")
            sys.exit(3)
        devices = self.getDevices()
        if (len(devices) < 1):
            eprint("No tablet devices were found")
            sys.exit(4)
        screens = self.getScreens()
        pass

    def getDevices(self) -> list:
        tempResult = subprocess.check_output(["xsetwacom", "--list",
                                              "devices"], bufsize=100).decode("utf-8")
        matches = re.findall(r"(.+)\tid: (\d+)\ttype:\s(.+)\s*", tempResult)
        results = []
        for m in matches:
            results.append(device(m[0], int(m[1]), m[2].strip()))
        return results

    def _getCurrOutput(self, device: device) -> str:
        pass

    def getScreens(self) -> list:
        monitors = screeninfo.get_monitors()
        totalWidth = 0
        totalHeight = 0
        results = []
        return results

    # def _getOutputList(self) -> list:
    #     pattern = re.compile(r"\S+")
    #     # note: may return invalid results if there is more than one xscreen
    #     tempResult = subprocess.check_output(
    #         ["xrandr"], bufsize=100).decode("utf-8")
    #     first = false
    #     results = []
    #     for line in tempResult.split('\n'):
    #         if first:
    #             first = False
    #             continue
    #         if line[0] == ' '
    #             continue
    #         results.append(pattern.search(line).group(0))

    #     return results

    def getMappedArea(self, device: device):
        call()
        result = transform()
        pass


if (__name__ == "__main__"):
    wiss = wiss()
    wiss.moveOutput(sys.argv[1:])
