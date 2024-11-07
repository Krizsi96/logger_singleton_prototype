"""
This module imports the singleton and module1.
The file path is specified so neither the default nor environment variables will be used.
"""
from pathlib import Path

from prototype.module1 import module_1_function
from prototype.singleton import FileWriter

file = FileWriter("module2", Path("file2.txt"))


def module_2_function() -> None:
    module_1_function()
    file.write("hello from module 2")


if __name__ == "__main__":
    module_2_function()
