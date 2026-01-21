'''

This is a placeholder for students to create their own implementation for
IPP-DEV-01-003: https://github.com/programming-in-python/ipp-exercise-tasks/issues/55

'''
import platform

system_name = platform.system()
machine_type = platform.machine()

print("system_name:", system_name)
print("machine_type:", machine_type)

import sys

python_version = sys.version
version_data = sys.version_info

print("python_version:", python_version)
print("version_data:", version_data)
