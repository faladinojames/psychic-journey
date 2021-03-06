# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import driver_authentication_pb2 as driver__authentication__pb2


class DriverRegistrationServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVehicleModelsOrMakes = channel.unary_unary(
                '/com.connectroutes.authentication.DriverRegistrationService/GetVehicleModelsOrMakes',
                request_serializer=driver__authentication__pb2.GetVehicleModelsOrMakesRequest.SerializeToString,
                response_deserializer=driver__authentication__pb2.GetVehicleModelsOrMakesResponse.FromString,
                )


class DriverRegistrationServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetVehicleModelsOrMakes(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DriverRegistrationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVehicleModelsOrMakes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVehicleModelsOrMakes,
                    request_deserializer=driver__authentication__pb2.GetVehicleModelsOrMakesRequest.FromString,
                    response_serializer=driver__authentication__pb2.GetVehicleModelsOrMakesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.connectroutes.authentication.DriverRegistrationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DriverRegistrationService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetVehicleModelsOrMakes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.connectroutes.authentication.DriverRegistrationService/GetVehicleModelsOrMakes',
            driver__authentication__pb2.GetVehicleModelsOrMakesRequest.SerializeToString,
            driver__authentication__pb2.GetVehicleModelsOrMakesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
