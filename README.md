my representation of unpack nested dictionaries

from this:

Dictionary = {'A': 1, 'B':{'C': 3, 'D': {'E': 5, 'F': 6}}}

to this:

Dictionary = {'A': 1, 'B_C': 3, 'B_D_E': 5, 'B_D_F': 6}