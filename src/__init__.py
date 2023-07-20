""" Anki add-on for generating TTS audio for selected text in the editor.

    This add-on adds a button to the editor toolbar that will generate TTS audio
    for the selected text in the editor. The audio is generated using the
    Google TTS API, and is saved to the media folder of the current collection.
    The audio is then added to the current note as a sound tag.
"""

__author__ = 'Marley Mulvin Broome'
__version__ = '0.0.1'
__license__ = 'MIT'
__email__ = "marley.developer@gmail.com"

from .util import sys_path_add, get_plugin_path

# Have to add the lib folder to the system path, so we can import gTTS
sys_path_add(get_plugin_path('lib'))

from .editor import add_editor_buttons
from .config import load_config

from anki.hooks import addHook

load_config(filename=get_plugin_path('config.ini'))

addHook('setupEditorButtons', add_editor_buttons)
