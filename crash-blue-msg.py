#############################################
#
#   Helmet Guardian: Impact Force Monitor
#
#############################################
# Code by jenfoxbot <jenfoxbot@gmail.com> Code is open-source, coffee/beerware Please keep header :) If you like the content, c$
#    buying me a coffee/beer if ya see me or contributing to my patreon (jenfoxbot) to support projects like this! :D
#############################################
#
# SO MANY THANKS to the wonderful folks who
#    make & document libraries.
#
####################################
# Libraries
####################################
#I2C library
import smbus as  smbus
#GPIO
import RPi.GPIO as GPIO
#Other
import time, os
#OS calls
import subprocess
####################################
#        User Parameters (Edit these as necessary)
####################################
#Set LIS331 address
addr = 0x19
#Set the acceleration range
maxScale = 24
#Set the LED GPIO pin
LED = 26
#Open file to save all data (creates new file in same folder if none and appends to existing file)
#allData = open("AllSensorData.txt", "a")
#Open file to save alert data (creates new file in same folder if none and appends to existing file)
#alrtData = open("AlertData.txt", "a")

#Set destination Bluetooth Mac Address
destBluetoothMacAddr = "FC:AA:B6:D3:62:FF"
targetBluetoothMacAddress = "FC:AA:B6:D3:62:FF"

# Open the socket and connect to destination device
import bluetooth


#port = 1
#print ("Connecting to device...")
#sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#sock.connect((targetBluetoothMacAddress, port))
#server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
#port = 1
#server_sock.bind(("",port))
#server_sock.listen(1)
  
#client_sock,address = server_sock.accept()
#print "Accepted connection from " + str(address)
  
#server_sock.connect((address, port))
#server_sock.send ("SOS")

#data = client_sock.recv(1024)
#print "received [%s]" % data
  
#client_sock.close()
#server_sock.close()

#print ("connection is done...")

####################################
# Initializations & Functions (Leave as-is unless you are
#   comfortable w/ code)
####################################
#LIS331 Constants (see Datasheet)
CTRL_REG1 = 0x20
CTRL_REG4 = 0x23
OUT_X_L = 0x28
OUT_X_H = 0x29
OUT_Y_L = 0x2A
OUT_Y_H = 0x2B
OUT_Z_L = 0x2C
OUT_Z_H = 0x2D
POWERMODE_NORMAL = 0x27
RANGE_6G = 0x00
RANGE_12G = 0x10
RANGE_24G = 0x30
# Create I2C bus
bus = smbus.SMBus(1)
#Initialize GPIO and turn GPIO 26 to low
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
#Initiliaze LIS331
def initialize(addr, maxScale):
    scale = int(maxScale)
    #Initialize accelerometer control register 1: Normal Power Mode and 50 Hz sample rate
    bus.write_byte_data(addr, CTRL_REG1, POWERMODE_NORMAL)
    #Initialize acceleromter scale selection (6g, 12 g, or 24g). This example uses 24g
    if maxScale == 6:
        bus.write_byte_data(addr, CTRL_REG4, RANGE_6G)
    elif maxScale == 12:
        bus.write_byte_data(addr, CTRL_REG4, RANGE_12G)

    elif maxScale == 24:
        bus.write_byte_data(addr, CTRL_REG4, RANGE_24G)
#        print ("Setting RANGE_24G")
    else:
        print ("Error in the scale provided -- please enter 6, 12, or 24")

#Function to read the data from accelerometer
def readAxes(addr):
    data0 = bus.read_byte_data(addr, OUT_X_L)
    data1 = bus.read_byte_data(addr, OUT_X_H)
    data2 = bus.read_byte_data(addr, OUT_Y_L)
    data3 = bus.read_byte_data(addr, OUT_Y_H)
    data4 = bus.read_byte_data(addr, OUT_Z_L)
    data5 = bus.read_byte_data(addr, OUT_Z_H)
    #Combine the two bytes and leftshit by 8
    x = data0 | data1 << 8
    y = data2 | data3 << 8
    z = data4 | data5 << 8
    #in case overflow
#    x=y=z=32000
    if x > 32767 :
        x -= 65536
    if y > 32767:
        y -= 65536
    if z > 32767 :
        z -= 65536
    #Calculate the two's complement as indicated in the datasheet
    x = ~x
    y = ~y
    z = ~z
    return x, y, z
#Function to calculate g-force from acceleration data
def convertToG(maxScale, xAccl, yAccl, zAccl):
    #Caclulate "g" force based on the scale set by user Eqn: (2*range*reading)/totalBits (e.g. 48*reading/2^16)
    X = (2*float(maxScale) * float(xAccl))/(2**16);
    Y = (2*float(maxScale) * float(yAccl))/(2**16);
    Z = (2*float(maxScale) * float(zAccl))/(2**16);
    return X, Y, Z

def isDanger(timestamp, x, y, z):
    counter = 0
    x = long(x)
    y = long(y)
    z = long(z)
#    print ("GPIO READ")
#    if abs(x) > 9 or abs(y) > 9 or abs(z) > 9:
#            alrtData.write(str(timestamp) + "\t" + "x: " + str(x) + "\t" + "y: " + str(y) + "\t" + "z: " + str(z) + "\n")
#            GPIO.output(LED, GPIO.HIGH)
#    elif abs(x) > 4 or abs(y) > 4 or abs(z) > 4:
    if abs(x) > 4 or abs(y) > 4 or abs(z) > 4:
            while abs(x) > 4 or abs(y) > 4 or abs(z) > 4:
                time_start = time.time()
                counter = counter + 1
                if counter > 4:
                    break
            time_end = time.time()
            if (counter > 4):
#                 print (" ")
#                 print (" ")
#                 print (" ")
#                 print (" ")
#                 print ("**************************************")
#                 print ("*                                    *")
#                 print ("*                                    *")
#                 print ("******   Sending SOS Message    ******")
#                 print ("*                                    *")
#                 print ("*                                    *")
#                 print ("**************************************")
#                 print (" ")
#                 print (" ")
#                 print (" ")
#                 print (" ")
#                alrtData.write(str(timestamp) + "\t" + "x: " + str(x) + "\t" + "y: " + str(y) + "\t" + "z: " + str(z) + "\n")
                 GPIO.output(LED, GPIO.HIGH)
#                 sendMessageTo(targetBluetoothMacAddress)
#                 lookUpNearbyBluetoothDevices()
                 subprocess.call ('echo Helmet2020-SoS Message > /dev/rfcomm0', shell=True)
#
# sudo apt-get install bluez python-bluez
# 
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/x232.html
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/c212.html

#import bluetooth

#def receiveMessages():
#  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#  
#  port = 1
#  server_sock.bind(("",port))
#  server_sock.listen(1)
#  
#  client_sock,address = server_sock.accept()
#  print "Accepted connection from " + str(address)
#  
#  data = client_sock.recv(1024)
#  print "received [%s]" % data
#  
#  client_sock.close()
#  server_sock.close()
#  
#def sendMessageTo(targetBluetoothMacAddress):
#  port = 1
#  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#  sock.connect((targetBluetoothMacAddress, port))
#  sock.send("smarthelmet2020-SOS")
#  sock.send("SOS")
#  sock.close()
  
#def lookUpNearbyBluetoothDevices():
#  print ("Look Up Near By Bluetooth Devices")
#  nearby_devices = bluetooth.discover_devices()
#  for bdaddr in nearby_devices:
#    print str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]"
#    if (str(bdaddr) == targetBluetoothMacAddress):
#      print ("Sending SOS message to this Mac Addr")
#      sendMessageTo(bdaddr)
#    GPIO.output(LED, GPIO.LOW)

    
    
#lookUpNearbyBluetoothDevices()
##receiveMessages()
#sendMessageTo(targetBluetoothMacAddress)


####################################
#       Main Function
####################################
def main():
    print ("Starting stream")
    subprocess.call ('sudo rfcomm listem hci0&', shell=True)
    while True:
        #initialize LIS331 accelerometer
        initialize(addr, 24)
        #Start timestamp
        ts = time.ctime()

        #Write timestamp to AllSensorData file

#        allData.write(str(ts) + "\t")
        #Get acceleration data for x, y, and z axes
        xAccl, yAccl, zAccl = readAxes(addr)
        #Calculate G force based on x, y, z acceleration data
        x, y, z = convertToG(maxScale, xAccl, yAccl, zAccl)
        #Determine if G force is dangerous to human body & take proper action
        isDanger(ts, x, y, z)
        #Write all sensor data to file AllSensorData (as you probably guessed :) )
 #       allData.write("x: " + str(x) + "\t" + "y: " + str(y) + "\t" + "z: " + str(z) + "\n")
        #print G values (don't need for full installation)
#        print ("Acceleration in X-Axis : %d" %x)
#        print ("Acceleration in Y-Axis : %d" %y)
#        print ("Acceleration in Z-Axis : %d" %z)
#        print ("\n")
        #Short delay to prevent overclocking computer
        time.sleep(0.2)
    #Run this program unless there is a keyboard interrupt
    try:
        while True:
            pass
    except KeyboardInterrupt:
        myprocess.kill()
        allData.close()
        alrtData.close()
        GPIO.cleanup()

if __name__ =="__main__":
    main()
#    allData.close()
#    alrtData.close()
    sock.close()
    GPIO.cleanup()
