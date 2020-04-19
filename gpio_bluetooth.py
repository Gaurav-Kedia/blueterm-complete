import bluetooth
import RPi.GPIO as GPIO

LED = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 0)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print "Accepted connection from ", address
while 1:
 data = client_socket.recv(1024)
 if(data == '0'):
  print ("GPIO 21 low, LED OFF")
#  server_socket.send("OFF\n")
  GPIO.output(LED,0)
 if(data == '1'):
  print ("GPIO 21 high, LED ON")
#  server_socket.send("ON\n")
  GPIO.output(LED,1)
 if(data == 'q'):
  print("quit")
  break;

client_socket.close()
server_socket.close()

