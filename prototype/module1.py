"""
This module only imports the singleton.
It doesn't specify the file path so it relies on environmental variables or the default file path.
"""

from prototype.singleton import FileWriter

file = FileWriter("module1")


def module_1_function() -> None:
    file.write("hello from module 1")


if __name__ == "__main__":
    module_1_function()
