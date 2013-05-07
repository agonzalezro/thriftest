import sys
sys.path.append('./gen-py')


from labsdirector import LabsDirector

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


try:
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

    caca = client.hello("PyGrunn")
    print "got %s" % "message"

    transport.close()
except Thrift.TException, tx:
    print "Exception: %s" % (tx.message)
