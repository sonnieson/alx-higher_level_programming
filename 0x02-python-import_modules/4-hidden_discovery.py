#!/usr/bin/python3
import marshal

def print_names_from_pyc(pyc_file):
    with open(pyc_file, 'rb') as file:
         code = marshal.load(file)
         names = [name for name in code.co_names if not name.startswith("__")]
         names.sort()
         for name in names:
             print(name)

if __name__ == "__main__":
    pyc_file = "hidden_4.pyc"  # Update with the correct path if needed
    print_names_from_pyc(pyc_file)
