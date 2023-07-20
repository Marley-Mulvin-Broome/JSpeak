from os.path import isfile as is_file, join as join_path

from aqt.utils import showInfo

from aqt.editor import Editor

from .config import get_resource, get_user_config
from .util import write_bytes_to_file
from .tts import get_current_tts


def append_tts_audio(editor: Editor):
    """ Reads the text in the selected field & text, generates TTS audio, and inserts it as a sound tag. """
    selection = editor.web.selectedText()

    if not selection:
        if editor.currentField is None:
            showInfo('Please select a field or highlight some text to generate audio.')
            return

        selection = editor.note.fields[editor.currentField]

    tts = get_current_tts()

    file_name = f"{repr(tts)}{selection}.mp3"

    media_path = editor.mw.col.media.dir()

    full_path = join_path(media_path, file_name)

    if not is_file(full_path):
        audio_bytes = tts.speak(selection)
        write_bytes_to_file(audio_bytes, full_path)

    # add [sound:file_name] to the target field
    # or the current field if no target field is selected
    target_field = get_user_config()["Target Field"]

    if not target_field:
        target_field = editor.currentField

    editor.web.eval(f'focusField("{target_field}")')

    if type(target_field) is not str:
        editor.note.fields[target_field] += f'[sound:{file_name}]'
    else:
        editor.note[target_field] += f'[sound:{file_name}]'

    editor.note.flush()

    editor.loadNoteKeepingFocus()


def add_editor_buttons(buttons, editor: Editor) -> None:
    """ Add buttons to the editor toolbar. """
    btn_audio = editor.addButton(
        get_resource('icon_file', get_full_path=True),
        'TTS Audio',
        append_tts_audio,
        tip='Generate TTS audio for selected text'
    )

    buttons.append(btn_audio)

    return buttons
