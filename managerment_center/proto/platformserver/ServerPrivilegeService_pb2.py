# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ServerPrivilegeService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ServerCommonMessage_pb2 as ServerCommonMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ServerPrivilegeService.proto',
  package='platformserver',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cServerPrivilegeService.proto\x12\x0eplatformserver\x1a\x19ServerCommonMessage.proto\"\x9f\x01\n\x14PrivilegeSaveRequest\x12\x10\n\x08parentId\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\nmoduleName\x18\x04 \x01(\t\x12\x16\n\x0esystemCategory\x18\x05 \x01(\x05\x12\x0c\n\x04type\x18\x06 \x01(\x05\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\x12\n\ncreateUser\x18\x08 \x01(\t\"\xad\x01\n\x16PrivilegeUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08parentId\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nmoduleName\x18\x05 \x01(\t\x12\x16\n\x0esystemCategory\x18\x06 \x01(\x05\x12\x0c\n\x04type\x18\x07 \x01(\x05\x12\x0b\n\x03url\x18\x08 \x01(\t\x12\x12\n\ncreateUser\x18\t \x01(\t\"$\n\x16PrivilegeDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xf8\x01\n\x16ServerPrivilegeService\x12\x46\n\x04save\x12$.platformserver.PrivilegeSaveRequest\x1a\x18.platformserver.Response\x12J\n\x06update\x12&.platformserver.PrivilegeUpdateRequest\x1a\x18.platformserver.Response\x12J\n\x06\x64\x65lete\x12&.platformserver.PrivilegeDeleteRequest\x1a\x18.platformserver.Responseb\x06proto3')
  ,
  dependencies=[ServerCommonMessage__pb2.DESCRIPTOR,])




_PRIVILEGESAVEREQUEST = _descriptor.Descriptor(
  name='PrivilegeSaveRequest',
  full_name='platformserver.PrivilegeSaveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parentId', full_name='platformserver.PrivilegeSaveRequest.parentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='platformserver.PrivilegeSaveRequest.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.PrivilegeSaveRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moduleName', full_name='platformserver.PrivilegeSaveRequest.moduleName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemCategory', full_name='platformserver.PrivilegeSaveRequest.systemCategory', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.PrivilegeSaveRequest.type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='platformserver.PrivilegeSaveRequest.url', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createUser', full_name='platformserver.PrivilegeSaveRequest.createUser', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=235,
)


_PRIVILEGEUPDATEREQUEST = _descriptor.Descriptor(
  name='PrivilegeUpdateRequest',
  full_name='platformserver.PrivilegeUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.PrivilegeUpdateRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentId', full_name='platformserver.PrivilegeUpdateRequest.parentId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='platformserver.PrivilegeUpdateRequest.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='platformserver.PrivilegeUpdateRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moduleName', full_name='platformserver.PrivilegeUpdateRequest.moduleName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemCategory', full_name='platformserver.PrivilegeUpdateRequest.systemCategory', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='platformserver.PrivilegeUpdateRequest.type', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='platformserver.PrivilegeUpdateRequest.url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createUser', full_name='platformserver.PrivilegeUpdateRequest.createUser', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=411,
)


_PRIVILEGEDELETEREQUEST = _descriptor.Descriptor(
  name='PrivilegeDeleteRequest',
  full_name='platformserver.PrivilegeDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='platformserver.PrivilegeDeleteRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=449,
)

DESCRIPTOR.message_types_by_name['PrivilegeSaveRequest'] = _PRIVILEGESAVEREQUEST
DESCRIPTOR.message_types_by_name['PrivilegeUpdateRequest'] = _PRIVILEGEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['PrivilegeDeleteRequest'] = _PRIVILEGEDELETEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrivilegeSaveRequest = _reflection.GeneratedProtocolMessageType('PrivilegeSaveRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRIVILEGESAVEREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.PrivilegeSaveRequest)
  ))
_sym_db.RegisterMessage(PrivilegeSaveRequest)

PrivilegeUpdateRequest = _reflection.GeneratedProtocolMessageType('PrivilegeUpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRIVILEGEUPDATEREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.PrivilegeUpdateRequest)
  ))
_sym_db.RegisterMessage(PrivilegeUpdateRequest)

PrivilegeDeleteRequest = _reflection.GeneratedProtocolMessageType('PrivilegeDeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRIVILEGEDELETEREQUEST,
  __module__ = 'ServerPrivilegeService_pb2'
  # @@protoc_insertion_point(class_scope:platformserver.PrivilegeDeleteRequest)
  ))
_sym_db.RegisterMessage(PrivilegeDeleteRequest)



_SERVERPRIVILEGESERVICE = _descriptor.ServiceDescriptor(
  name='ServerPrivilegeService',
  full_name='platformserver.ServerPrivilegeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=452,
  serialized_end=700,
  methods=[
  _descriptor.MethodDescriptor(
    name='save',
    full_name='platformserver.ServerPrivilegeService.save',
    index=0,
    containing_service=None,
    input_type=_PRIVILEGESAVEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='platformserver.ServerPrivilegeService.update',
    index=1,
    containing_service=None,
    input_type=_PRIVILEGEUPDATEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='platformserver.ServerPrivilegeService.delete',
    index=2,
    containing_service=None,
    input_type=_PRIVILEGEDELETEREQUEST,
    output_type=ServerCommonMessage__pb2._RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERPRIVILEGESERVICE)

DESCRIPTOR.services_by_name['ServerPrivilegeService'] = _SERVERPRIVILEGESERVICE

# @@protoc_insertion_point(module_scope)