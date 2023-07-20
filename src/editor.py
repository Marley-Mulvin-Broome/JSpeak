from os.path import isfile as is_file, join as join_path

from aqt.utils import showInfo
from aqt import mw
from aqt.editor import Editor

from .config import get_resource, get_user_config
from .speak.ttsprovider import ITTSProvider
from .util import write_bytes_to_file
from .tts import get_current_tts


def parse_target_field(target_field: str) -> list[str]:
    """ Parse the target field from the config. """
    if not target_field or target_field is None:
        return []

    target_field = target_field.strip().split('|')

    if len(target_field) == 0:
        return []

    return target_field


def pick_target_field(fields: list[str], targets: list[str], fallback: str) -> str:
    """ Pick the target field from the list of fields.
    If the target field is not in the list of fields, return the fallback.
    Priority is given to the first field in the list of fields.
    """
    for target in targets:
        if target in fields:
            return target

    return fallback


def generate_tts_file(text: str, filename: str, tts: ITTSProvider = None) -> str:
    """ Generate a TTS file from the given text and TTS provider. """
    if tts is None:
        tts = get_current_tts()

    full_path = join_path(mw.col.media.dir(), filename)

    if not is_file(full_path):
        audio_bytes = tts.speak(text)
        write_bytes_to_file(audio_bytes, full_path)

    return full_path


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

    generate_tts_file(selection, file_name, tts)

    target_field = pick_target_field(
        editor.note.keys(),
        parse_target_field(get_user_config()["Target Field"]),
        ""
    )

    if not target_field:
        target_field = editor.note.keys()[editor.currentField]

    if len(editor.note[target_field]) > 0:
        target_field = editor.note.keys()[editor.currentField]

    editor.web.eval(f'focusField("{target_field}")')
    editor.note[target_field] += f'[sound:{file_name}]'
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
