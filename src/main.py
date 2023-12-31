from sys import modules as loaded_modules


def main():
    # If we are running tests do not
    # run addon because the tests will crash
    if "pytest" in loaded_modules:
        return

    from .util import sys_path_add, get_plugin_path
    from .config import load_config, get_config, get_user_config

    load_config(filename=get_plugin_path("config.ini"))

    # Have to add the lib folder to the system path, so we can import gTTS
    sys_path_add(get_plugin_path(get_config().get("Info", "lib_path")))

    from .editor import add_editor_buttons
    from .addonauthenticator import authenticate_config_hook
    from aqt.gui_hooks import (
        editor_did_init_buttons,
        addon_config_editor_will_update_json,
    )

    editor_did_init_buttons.append(add_editor_buttons)
    addon_config_editor_will_update_json.append(authenticate_config_hook)
