from configparser import ConfigParser
from os.path import isfile as is_file
from aqt import mw

from .util import get_plugin_path

_config = ConfigParser()
_last_filename = ""


def config_loaded(func):
    """Decorator to ensure the config has been loaded before calling the decorated function."""

    def wrapper(*args, **kwargs):
        if len(_config.sections()) == 0:
            raise RuntimeError("Config not loaded")

        return func(*args, **kwargs)

    return wrapper


def load_config(filename="config.ini") -> None:
    """Load the config file."""
    if not is_file(filename):
        raise FileNotFoundError(f"Config file not found ({filename})")

    _config.read(filename)

    if len(_config.sections()) == 0:
        raise ValueError(f"Config file is empty ({filename})")

    global _last_filename
    _last_filename = filename


def get_last_config_filename() -> str:
    """Get the last config filename."""
    return _last_filename


def clear_config() -> None:
    """Clear the config."""
    _config.clear()


@config_loaded
def get_config() -> ConfigParser:
    """Get the config parser."""
    return _config


@config_loaded
def get_resource(resource_name: str, get_full_path=True) -> str:
    """Get the path to a resource."""
    local_path = _config.get("Resources", resource_name, fallback="")

    if len(local_path) == 0:
        raise ValueError("Resource not found")

    # need to do this so if we join it doesn't break
    if local_path.startswith("/"):
        local_path = local_path[1:]

    if get_full_path:
        return get_plugin_path(to_join=local_path)

    return local_path


@config_loaded
def save_config(filename="config.ini") -> None:
    """Save the config file."""
    with open(filename, "w") as config_file:
        _config.write(config_file)


# Anki user config


def get_user_config():
    """Get the user config stored in config.json."""
    return mw.addonManager.getConfig(__name__)
