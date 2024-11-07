"""
This module imports the singleton and both of the other modules.
The file path is set at the global space but with option it is changed at run time.
"""
from pathlib import Path
from typing import Annotated

from prototype.module1 import module_1_function
from prototype.module2 import module_2_function
from prototype.singleton import FileWriter

import typer

NAME = Path(__file__).name.removesuffix(".py")
file = FileWriter(NAME, Path("file3.txt"))

FILE_NAME_OPTION_WAS_GIVEN = True


def module_3_function(
        file_path: Annotated[Path, typer.Option()] = None,
) -> None:
    if file_path:
        file.__init__(NAME, Path(file_path))
    module_1_function()
    module_2_function()
    file.write("hello from module 3")


if __name__ == "__main__":
    typer.run(module_3_function)
