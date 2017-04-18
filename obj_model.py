#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import singleton

class Model( object ):
	def __init__(self):
		super().__init__()

	def writeOnSingleton(self,text):
		singleton.foo = text

	def readFromSingleton(self,singletonVar):
		print(singletonVar)

	def otherAmazingStuff(self,yourDreams):
		pass
