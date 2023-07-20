from unittest.mock import Mock, MagicMock

import src
from src.config import load_config, save_config, clear_config, get_resource, get_config, get_user_config, get_last_config_filename
from os.path import join as join_path, dirname, realpath

import pytest

config_text = """;
; Description: Non-user-editable configuration file for JSpeak
[DEFAULT]
lib_path = lib

[Resources]
icon_file = icons/jspeak.ico.png.qrt
"""


@pytest.fixture(autouse=True)
def load_config_fixture(tmp_path):
    file = tmp_path / 'config.ini'
    file.write_text(config_text)

    load_config(file)
    yield
    clear_config()


def test_get_resource(mocker):
    def mocked_get_plugin_path(to_join: str = "") -> str:
        return join_path("/anki2/addons21/jspeak", to_join)

    mocker.patch('src.config.get_plugin_path', mocked_get_plugin_path)

    assert get_resource('icon_file', get_full_path=False) == 'icons/jspeak.ico.png.qrt'
    assert get_resource('icon_file', get_full_path=True) == '/anki2/addons21/jspeak/icons/jspeak.ico.png.qrt'



def test_get_resource_not_found():
    with pytest.raises(ValueError):
        get_resource('not_found')


def test_get_resource_not_loaded():
    clear_config()

    with pytest.raises(RuntimeError):
        get_resource('not_found')


def test_get_config_not_loaded():
    clear_config()

    with pytest.raises(RuntimeError):
        get_config()


def test_save_config():
    get_config()['Poop'] = {"cat": "wow"}
    save_config(get_last_config_filename())
    assert get_config().get('Poop', 'cat') == 'wow'

    clear_config()
    load_config(get_last_config_filename())
    assert get_config().get('Poop', 'cat') == 'wow'


def test_clear(datafiles):
    # unsaved change
    get_config()['Poop'] = {"cat": "wow"}
    clear_config()
    load_config(get_last_config_filename())
    assert 'Poop' not in get_config().sections()


def test_load_config_not_found():
    with pytest.raises(FileNotFoundError):
        load_config('not_found.ini')


def test_load_config_empty(tmp_path):
    file = tmp_path / 'config.ini'
    file.write_text('')

    clear_config()

    with pytest.raises(ValueError):
        load_config(filename=file)


def test_get_user_config(mocker):
    class MockedConfig:
        def __init__(self):
            self.addonManager = Mock()
            self.addonManager.getConfig = MagicMock(return_value={'tree': 'poop'})

    mocker.patch("src.config.mw", MockedConfig())

    assert get_user_config() == {'tree': 'poop'}
