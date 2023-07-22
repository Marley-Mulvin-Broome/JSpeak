""" Anki add-on for generating TTS audio for selected text in the editor.

    This add-on adds a button to the editor toolbar that will generate TTS audio
    for the selected text in the editor. The audio is generated using the
    Google TTS API, and is saved to the media folder of the current collection.
    The audio is then added to the current note as a sound tag.
"""

__author__ = "Marley Mulvin Broome"
__version__ = "0.0.1"
__license__ = "MIT"
__email__ = "marley.developer@gmail.com"
__credits__ = ["www.freepik.com"]

from .main import main as entry_point

entry_point()
