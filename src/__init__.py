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

from anki.hooks import addHook

from src.util import sys_path_add, get_plugin_path
# Add to sys.path, so we can import our libraries
sys_path_add(get_plugin_path('lib'))

from src.editor import add_editor_buttons
from src.config import load_config



load_config()

addHook('setupEditorButtons', add_editor_buttons)
