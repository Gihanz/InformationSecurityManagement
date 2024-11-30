#!/usr/bin/env python3

import platform

'''
identifying the underlying platform,
can propvide aliased and terse can turn 
aliased and terse on (0) and off (1). 

'''
print(platform.platform(aliased=0, terse=0))

#gets the release of the OS
print(platform.release())

#Returns the os name
print(platform.system())

# gets version of python
print(platform.python_version())

print(platform.machine())

print(platform.node())

print(platform.uname() )

