import sys

collections = {"list": list(), "tuple": tuple(), "dict": dict(), "set": set()}

for name, collection in collections.items():
    print(f'{name} = {sys.getsizeof(collection)} bytes')