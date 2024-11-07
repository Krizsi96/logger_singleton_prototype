import inspect
import os
import tempfile
from pathlib import Path


DEFAULT_FILE_PATH = Path(os.environ.get(
    "DEMO_FILE_PATH", Path(tempfile.gettempdir()) / "demo" / "demo.txt"
))

class FileWriter(object):
    def __new__(cls, name: str, file: Path = DEFAULT_FILE_PATH):
        print("new method for FileWriter")
        if not hasattr(cls, "instance"):
            print("Creating a new FileWriter object")
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name: str, file: Path = DEFAULT_FILE_PATH) -> None:
        print("Initializing FileWriter object")
        try:
            if self.file_path:
                print("Delete previous log file")
                self.file_path.unlink()
        except AttributeError:
            pass
        create_parent_directory_if_not_there(file)
        self.file_path = file
        print("Open new log file")
        self.file = file.open("w")
        self.name = name
        print(f"FileWriter: {self.name=}, {self.file_path=}")

    def write(self, string: str) -> None:
        modules = "/log"
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        try:
            module_name = mod.__name__
            module_name = module_name.split(".")
            for module in module_name:
                if module == "__main__":
                    modules += f"/{self.name}"
                else:
                    modules += f"/{module}"
        except AttributeError:
            pass
        print(f"Writing to file from {modules}")
        self.file.write(f"{modules} : {string}\n")

    def __del__(self) -> None:
        self.write("finished")
        self.file.close()

def create_parent_directory_if_not_there(path: Path) -> None:
    """
    Creates a parent directory if it does not exist.

    Args:
        path: The path of the file with the parent directory.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
