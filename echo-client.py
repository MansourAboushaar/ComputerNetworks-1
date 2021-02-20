import socket
from datetime import datetime

def delta_time(time_2,time_1):
    time_delta = time_2 - time_1 # Time difference
    RTT = (time_delta.total_seconds())*1000 # Time in milliseconds
    return RTT
    
    
# Message to be sent from Client to Server
msgFromClient_1       = "UDP ECHO_1"
msgFromClient_2       = "UDP ECHO_2"
msgFromClient_3       = "UDP ECHO_3"
msgFromClient_4       = "UDP ECHO_4"
msgFromClient_5       = "UDP ECHO_5"
#Encoding
bytesToSend_1       = str.encode(msgFromClient_1)
bytesToSend_2       = str.encode(msgFromClient_2)
bytesToSend_3       = str.encode(msgFromClient_3)
bytesToSend_4       = str.encode(msgFromClient_4)
bytesToSend_5       = str.encode(msgFromClient_5)

#Local Address and port number different to 7
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

#FIRST ECHO
echo_1 = datetime.now() #Time of sending the ECHO
UDPClientSocket.sendto(bytesToSend_1, serverAddressPort) #Sending the ECHO 
msgFromServer = UDPClientSocket.recvfrom(bufferSize) #Receiving the ECHO back
echo_1_server = datetime.now() #Time of receiving the ECHO
RTT_1 = delta_time(echo_1_server,echo_1)

#SECOND ECHO
echo_2 = datetime.now() #Time of sending the ECHO
UDPClientSocket.sendto(bytesToSend_2, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
echo_2_server = datetime.now() #Time of receiving the ECHO
RTT_2 = delta_time(echo_2_server,echo_2)

#THIRD ECHO
echo_3 = datetime.now() #Time of sending the ECHO
UDPClientSocket.sendto(bytesToSend_3, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
echo_3_server = datetime.now() #Time of receiving the ECHO
RTT_3 = delta_time(echo_3_server,echo_3)

#FOURTH ECHO
echo_4 = datetime.now() #Time of sending the ECHO
UDPClientSocket.sendto(bytesToSend_4, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
echo_4_server = datetime.now() #Time of receiving the ECHO
RTT_4 = delta_time(echo_4_server,echo_4)

#FIFTH ECHO
echo_5 = datetime.now() #Time of sending the ECHO
UDPClientSocket.sendto(bytesToSend_5, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
echo_5_server = datetime.now() #Time of receiving the ECHO
RTT_5 = delta_time(echo_5_server,echo_5)

########################################################
msg = "Message from Server {}".format(msgFromServer[0])
Average_RTT = (RTT_1 + RTT_2 + RTT_3 + RTT_4 + RTT_5) / 5 

print(msg)
print("echo_1:",echo_1, "echo_1_server",echo_1_server,"RTT_1=",RTT_1)
print("echo_2:",echo_2, "echo_2_server",echo_2_server,"RTT_2=",RTT_2)
print("echo_3:",echo_3, "echo_3_server",echo_3_server,"RTT_3=",RTT_3)
print("echo_4:",echo_4, "echo_4_server",echo_4_server,"RTT_4=",RTT_4)
print("echo_5:",echo_5, "echo_5_server",echo_5_server,"RTT_5=",RTT_5)
print("\nThe average RTT of the 5 ECHOS is :", Average_RTT)
