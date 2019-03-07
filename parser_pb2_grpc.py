# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import parser_pb2 as parser__pb2


class ParserStub(object):
  """The parser service takes several results from Microsoft OCR and performs
  clustering to determine which parts are important.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.parse = channel.unary_unary(
        '/Parser/parse',
        request_serializer=parser__pb2.ParseRequest.SerializeToString,
        response_deserializer=parser__pb2.ParseReply.FromString,
        )


class ParserServicer(object):
  """The parser service takes several results from Microsoft OCR and performs
  clustering to determine which parts are important.
  """

  def parse(self, request, context):
    """Parse several pages and return the important paragraphs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ParserServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'parse': grpc.unary_unary_rpc_method_handler(
          servicer.parse,
          request_deserializer=parser__pb2.ParseRequest.FromString,
          response_serializer=parser__pb2.ParseReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Parser', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
