# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from .parse_pb2 import(
    LocustChange as parse_pb2___LocustChange,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class IndexKey(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    filepath: typing___Text = ...
    name: typing___Text = ...
    line: builtin___int = ...
    revision: typing___Text = ...

    def __init__(self,
        *,
        filepath : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        line : typing___Optional[builtin___int] = None,
        revision : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"filepath",b"filepath",u"line",b"line",u"name",b"name",u"revision",b"revision"]) -> None: ...
type___IndexKey = IndexKey

class NestedChange(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def key(self) -> type___IndexKey: ...

    @property
    def change(self) -> parse_pb2___LocustChange: ...

    @property
    def children(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___NestedChange]: ...

    def __init__(self,
        *,
        key : typing___Optional[type___IndexKey] = None,
        change : typing___Optional[parse_pb2___LocustChange] = None,
        children : typing___Optional[typing___Iterable[type___NestedChange]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"change",b"change",u"key",b"key"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"change",b"change",u"children",b"children",u"key",b"key"]) -> None: ...
type___NestedChange = NestedChange