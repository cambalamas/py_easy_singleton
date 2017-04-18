#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import singleton
from obj_view import View
from obj_model import Model

if __name__ == '__main__':

	v = View()
	m = Model()
	print( singleton.foo )


	# Edit via obj1 instance.

	v.writeOnSingleton('var1')

	print( singleton.foo )
	v.readFromSingleton( singleton.foo )
	m.readFromSingleton( singleton.foo )


	# Edit via obj2 instance.

	m.writeOnSingleton('var2')

	print( singleton.foo )
	v.readFromSingleton( singleton.foo )
	m.readFromSingleton( singleton.foo )

	# ;)
	print( singleton.bar )
