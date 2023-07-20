from gtts.tts import gTTS
from gtts.lang import tts_langs

from .ttsprovider import ITTSProvider


class GoogleTTS(ITTSProvider):
    """ Google TTS provider."""

    def speak(self, text, **kwargs):
        """ Speak the given text."""
        lang = kwargs.get('lang')

        if not lang:
            lang = 'ja'

        return gTTS(text=text, lang=lang).stream()

    def get_languages(self):
        """ Get a list of available languages."""
        return tts_langs()

    def __repr__(self):
        return 'Google'
