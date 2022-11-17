s1 = "Mubeen"
print(id(s1), s1)

id_1 = id(s1)

s1 = "Ahmad"
print(id(s1), s1)

id_2 = id(s1)

print("\n")
import ctypes

print("Previous String", ctypes.cast(id_1, ctypes.py_object).value)
print("New String", ctypes.cast(id_2, ctypes.py_object).value)

import time
print("Wait 1 sec garbage collector change the address of previous")

del s1
time.sleep(5)
for i in range(100000):
    ...
time.sleep(5)

print(id("Mubeen"))