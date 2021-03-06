# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: driver-authentication.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='driver-authentication.proto',
  package='com.connectroutes.authentication',
  syntax='proto3',
  serialized_options=b'Z\005proto',
  serialized_pb=b'\n\x1b\x64river-authentication.proto\x12 com.connectroutes.authentication\".\n\x1eGetVehicleModelsOrMakesRequest\x12\x0c\n\x04make\x18\x01 \x01(\t\"8\n\x1fGetVehicleModelsOrMakesResponse\x12\x15\n\rvehicle_names\x18\x01 \x03(\t2\xbe\x01\n\x19\x44riverRegistrationService\x12\xa0\x01\n\x17GetVehicleModelsOrMakes\x12@.com.connectroutes.authentication.GetVehicleModelsOrMakesRequest\x1a\x41.com.connectroutes.authentication.GetVehicleModelsOrMakesResponse\"\x00\x42\x07Z\x05protob\x06proto3'
)




_GETVEHICLEMODELSORMAKESREQUEST = _descriptor.Descriptor(
  name='GetVehicleModelsOrMakesRequest',
  full_name='com.connectroutes.authentication.GetVehicleModelsOrMakesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='make', full_name='com.connectroutes.authentication.GetVehicleModelsOrMakesRequest.make', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=65,
  serialized_end=111,
)


_GETVEHICLEMODELSORMAKESRESPONSE = _descriptor.Descriptor(
  name='GetVehicleModelsOrMakesResponse',
  full_name='com.connectroutes.authentication.GetVehicleModelsOrMakesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vehicle_names', full_name='com.connectroutes.authentication.GetVehicleModelsOrMakesResponse.vehicle_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=113,
  serialized_end=169,
)

DESCRIPTOR.message_types_by_name['GetVehicleModelsOrMakesRequest'] = _GETVEHICLEMODELSORMAKESREQUEST
DESCRIPTOR.message_types_by_name['GetVehicleModelsOrMakesResponse'] = _GETVEHICLEMODELSORMAKESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVehicleModelsOrMakesRequest = _reflection.GeneratedProtocolMessageType('GetVehicleModelsOrMakesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVEHICLEMODELSORMAKESREQUEST,
  '__module__' : 'driver_authentication_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.authentication.GetVehicleModelsOrMakesRequest)
  })
_sym_db.RegisterMessage(GetVehicleModelsOrMakesRequest)

GetVehicleModelsOrMakesResponse = _reflection.GeneratedProtocolMessageType('GetVehicleModelsOrMakesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVEHICLEMODELSORMAKESRESPONSE,
  '__module__' : 'driver_authentication_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.authentication.GetVehicleModelsOrMakesResponse)
  })
_sym_db.RegisterMessage(GetVehicleModelsOrMakesResponse)


DESCRIPTOR._options = None

_DRIVERREGISTRATIONSERVICE = _descriptor.ServiceDescriptor(
  name='DriverRegistrationService',
  full_name='com.connectroutes.authentication.DriverRegistrationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=172,
  serialized_end=362,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetVehicleModelsOrMakes',
    full_name='com.connectroutes.authentication.DriverRegistrationService.GetVehicleModelsOrMakes',
    index=0,
    containing_service=None,
    input_type=_GETVEHICLEMODELSORMAKESREQUEST,
    output_type=_GETVEHICLEMODELSORMAKESRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DRIVERREGISTRATIONSERVICE)

DESCRIPTOR.services_by_name['DriverRegistrationService'] = _DRIVERREGISTRATIONSERVICE

# @@protoc_insertion_point(module_scope)
