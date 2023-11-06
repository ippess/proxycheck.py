from typing import Dict, Union


class BaseFlags:
    VALID_FLAGS: [str] = ["vpn", "asn", "cur", "node", "time", "risk", "port", "seen", "short", "p", "days", "tag",
                          "ver"]

    _flags: Dict[str, int]

    __slots__ = ("_flags",)

    def __init__(self, **kwargs: Union[int, bool]):
        self._flags = {}
        for key, value in kwargs.items():
            if key not in self.VALID_FLAGS:
                raise ValueError(f"Invalid flag {key}")
            self._flags[key] = int(value)
            setattr(self, key, int(value))

    def __repr__(self):
        return f"<Flags {self._flags}>"


class Flags(BaseFlags):

    def __init__(self, **kwargs: Union[int, bool]):
        super().__init__(**kwargs)

    @classmethod
    def most_info(cls):
        return cls(
            vpn=3,
            asn=True,
            node=True,
            port=True,
            seen=True,
            risk=2
        )

    @classmethod
    def none(cls):
        return cls()

    @classmethod
    def default(cls):
        return cls(
            vpn=True,
            asn=True,
            node=True,
            port=True,
            seen=True,
            risk=True
        )

    @classmethod
    def from_dict(cls, flags: Dict[str, Union[int, bool]]):
        return cls(**flags)

    def to_dict(self):
        return self._flags
