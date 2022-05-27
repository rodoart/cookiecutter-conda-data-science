from pathlib import Path
from typing import Callable

def make_dir_function(
    dir_name= '',
    workspace=''
) -> Callable[..., Path]:
    """Generate a function that converts a string or iterable of strings into
    a path relative to the project directory.

    Args:
        dirname: Name of the subdirectories to extend the path of the main
            project.
            If an iterable of strings is passed as an argument, then it is
            collapsed to a single steing with anchors dependent on the
            operating system.
        
        workspace: Path of the workspace. If it is none, the folder in which the 
            file that is being executed is located is taken.

    Returns:
        A function that returns the path relative to a directory that can
        receive `n` number of arguments for expansion.
    """

    if workspace:
        workspace_path = Path(workspace).resolve()
    else:
        workspace_path = Path('.').resolve()

    def dir_path(*args) -> Path:
        if isinstance(dir_name, str):
            return workspace_path.joinpath(dir_name, *args)
        else:
            return workspace_path.joinpath(*dir_name, *args)

    return dir_path

project_dir = make_dir_function("")

for dir_type in [
        ["data"],
        ["data", "raw"],
        ["data", "processed"],
        ["data", "interim"],
        ["data", "external"],
        ["models"],
        ["notebooks"],
        ["references"],
        ["reports"],
        ["reports", "figures"]
    ]:
    dir_var = '_'.join(dir_type) + "_dir"
    exec(f"{dir_var} = make_dir_function({dir_type})")