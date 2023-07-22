def main():
    from sys import modules as loaded_modules

    # If we are running tests do not
    # run addon because the tests will crash
    if "pytest" in loaded_modules:
        return

    from .util import sys_path_add, get_plugin_path
    from .config import load_config, get_config

    load_config(filename=get_plugin_path("config.ini"))

    # Have to add the lib folder to the system path, so we can import gTTS
    sys_path_add(get_plugin_path(get_config().get("Info", "lib_path")))

    from .editor import add_editor_buttons
    from anki.hooks import addHook

    addHook("setupEditorButtons", add_editor_buttons)
