from .config import get_user_config
from .speak.ttsprovider import ITTSProvider
from .speak.googletts import GoogleTTS


def get_tts_provider(name: str) -> ITTSProvider:
    name = name.lower()

    if name == 'google':
        return GoogleTTS()

    raise ValueError(f'Unknown TTS provider: {name}')


def get_current_tts() -> ITTSProvider:
    """ Get the current TTS provider."""
    return _current_tts


_current_tts = get_tts_provider(get_user_config()['TTS Engine'])
