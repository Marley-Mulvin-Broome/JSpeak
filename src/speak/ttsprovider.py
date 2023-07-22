from typing import Dict as Dict_t
from abc import abstractmethod, ABCMeta


class ITTSProvider(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is ITTSProvider:
            return (
                hasattr(subclass, "speak")
                and callable(subclass.speak)
                and hasattr(subclass, "get_languages")
                and callable(subclass.get_languages)
                or NotImplemented
            )

    @abstractmethod
    def speak(self, text: str, **kwargs):
        """Speak the given text."""
        raise NotImplementedError

    @abstractmethod
    def get_languages(self) -> Dict_t:
        """Get a list of available languages."""
        raise NotImplementedError
