import sys
import re
import alpha.mathlib.geometry as geometry  #  geometry.py

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module search order
# 1. current folder
# 2. folders in PYTHONPATH
# 3. <INSTALL-FOLDER>/lib

print(f"{sys.prefix = }\n")
for path in sys.path:
    print(path)
print()

print(f"{sys.modules['alpha.mathlib.geometry'] = }")
print(f"{sys.modules['sys'] = }")
print(f"{sys.modules['re'] = }")
