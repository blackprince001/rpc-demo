from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MenuRequest(_message.Message):
    __slots__ = ("plantain", "rice", "beans", "vegetables")
    PLANTAIN_FIELD_NUMBER: _ClassVar[int]
    RICE_FIELD_NUMBER: _ClassVar[int]
    BEANS_FIELD_NUMBER: _ClassVar[int]
    VEGETABLES_FIELD_NUMBER: _ClassVar[int]
    plantain: int
    rice: int
    beans: int
    vegetables: bool
    def __init__(self, plantain: _Optional[int] = ..., rice: _Optional[int] = ..., beans: _Optional[int] = ..., vegetables: bool = ...) -> None: ...

class MenuResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
