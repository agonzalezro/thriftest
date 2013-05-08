import sys
sys.path.append('./gen-py')


from labsdirector import LabsDirector
from labsdirector.ttypes import ThisIsSparta

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


try:
    # This was not forgotten, it's to make an step by step demo :)
    import ipdb
    ipdb.set_trace()

    # Make socket
    transport = TSocket.TSocket('localhost', 9999)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TFramedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = LabsDirector.Client(protocol)

    # Connect!
    transport.open()

    response = client.hello("PyGrunn")

    try:
        client.bye()
    except ThisIsSparta as exception:
        print "We got this Exception from Scala: %s" % exception.message

    transport.close()
except Thrift.TException as exception:
    print "This is an complete unexpected Exception: %s" % (exception.message)
