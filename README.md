# M11 T1: Class Composition Assignment

## Instructions for students

- Implement your solutions in `assignment.py`
- The tests in `test_assignment.py` can be inspected but do not modify them

### Directions - Copy/Pasted from Canvas

* Review disk_space.py
* Review memory.py
* finish the code in assignment.py

Primary goal is to create a `Memory` and a `DiskSpace` object. Then pass those into a `Computer` object.

Said another way; we have created classes/objects that contain no parameters, then have passed in built ins (str, int, float, etc.)
Now we will pass in other objects we created; so we have:
- `Memory` made out of builtins
- `DiskSpace` made out of builtins
- `Computer` made out of a (`str`, `DiskSpace`, `Memory`)