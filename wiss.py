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

class __device:
	def __init__(self, name, id, type):
		self.name = name;
		self.id = id;
		self.type = type;
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
			self.__usage();
			sys.exit(2);
		pass
	
	def __getDevices(self):
		
		pass
	
	def __getMappedArea(self, device: __device):
		device.
		results = [];
		pass
	
	
	
	  
	  
	  
if (__name__ == "__main__"):
	wiss = wiss()
	wiss.moveOutput(sys.argv[1:])
