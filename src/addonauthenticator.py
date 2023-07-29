from aqt.utils import showCritical
from json import loads as load_json

REQUIRED_USER_CONFIG_KEYS = [
    "TTS Language",
    "TTS Engine",
    "Target Field",
    "Preview",
    "Overwrite Existing Audio",
]


def authenticate_config_hook(text: str, addon: str) -> str:
    """Authenticate the config."""

    if addon != "JSpeak":
        return text

    user_config = load_json(text)

    missing_keys, invalid_keys = authenticate_config(user_config)

    error_report = "There were some errors found in your config."

    # this should never run because Anki keeps removed keys in the config
    if missing_keys:
        missing_keys_str = ", ".join(missing_keys)
        error_report += "\n\nMissing keys: " + missing_keys_str
        error_report += "\n Please add these keys to your config."

    if invalid_keys:
        invalid_keys_str = ", ".join(invalid_keys)
        error_report += "\n\nInvalid keys: " + invalid_keys_str
        error_report += "\n Please remove these keys from your config."

    if missing_keys or invalid_keys:
        showCritical(error_report)

    print(user_config)

    return text


def authenticate_config(
    config_dictionary: dict[str, any]
) -> tuple[list[str], list[str]]:
    """Authenticate the config dictionary."""
    missing_keys = []
    invalid_keys = []

    for key in REQUIRED_USER_CONFIG_KEYS:
        if key not in config_dictionary:
            missing_keys.append(key)

    for key in config_dictionary:
        if key not in REQUIRED_USER_CONFIG_KEYS:
            invalid_keys.append(key)

    return missing_keys, invalid_keys
