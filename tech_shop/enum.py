from enum import Enum


class DjangoEnum(Enum):
    """Extend this enumeration for models choice fields """
    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]
