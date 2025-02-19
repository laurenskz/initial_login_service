from grpc import insecure_channel

from com.baboea.services.login_service_pb2 import InitialLoginForm
from com.baboea.services.login_service_pb2_grpc import UserInitServiceStub

if __name__ == '__main__':
    bbb = UserInitServiceStub(insecure_channel("192.168.1.153:50054"))
    print(bbb.SetupUser(InitialLoginForm()))