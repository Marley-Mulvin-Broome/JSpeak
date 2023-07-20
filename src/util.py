from os.path import dirname, realpath, join as join_path, isdir as is_dir
from sys import path as lib_path


def sys_path_add(directory: str) -> None:
    """ Add a directory to the system path."""
    if not is_dir(directory):
        raise NotADirectoryError(f"Directory '{directory}' does not exist")

    lib_path.append(directory)


def get_plugin_path(to_join: str = "") -> str:
    """ Get the path to this plugin."""
    return join_path(dirname(realpath(__file__)), to_join)


def write_bytes_to_file(stream, filename: str) -> None:
    """ Write a binary stream to a file."""
    with open(filename, 'wb') as f:
        for chunk in stream:
            f.write(chunk)

