#UDP Server echoing incoming UDP messages
# https://www.waveshare.com/pico-eth-ch9121.htm
# https://www.waveshare.com/wiki/Pico-ETH-CH9121
#https://www.waveshare.com/w/upload/e/ef/CH9121_SPCC.pdf


from machine import UART, Pin
import time

message = 'hello world'


uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

CFG = Pin(14, Pin.OUT,Pin.PULL_UP)
RST = Pin(17, Pin.OUT,Pin.PULL_UP)
RST.value(1)

MODE = 2  #0:TCP Server 1:TCP Client 2:UDP Server 3:UDP Client
GATEWAY = (192, 168, 0, 1)   # GATEWAY
TARGET_IP = (192, 168, 0, 87)# TARGET_IP
LOCAL_IP = (192, 168, 0, 122)    # LOCAL_IP
SUBNET_MASK = (255,255,255,0) # SUBNET_MASK
LOCAL_PORT1 = 5001             # LOCAL_PORT1
LOCAL_PORT2 = 4001             # LOCAL_PORT2
TARGET_PORT = 8080            # TARGET_PORT
#BAUD_RATE = 115200            # BAUD_RATE
BAUD_RATE = 9600            # BAUD_RATE  change to 9600 and it now works




print("config begin")
CFG.value(0) #begin config
time.sleep(0.1)
uart0.write(b'\x57\xab\x10'+MODE.to_bytes(1, 'little'))
time.sleep(0.1)
uart0.write(b'\x57\xab\x11'+bytes(bytearray(LOCAL_IP)))
time.sleep(0.1)
uart0.write(b'\x57\xab\x12'+bytes(bytearray(SUBNET_MASK)))
time.sleep(0.1)
uart0.write(b'\x57\xab\x13'+bytes(bytearray(GATEWAY)))
time.sleep(0.1)
uart0.write(b'\x57\xab\x14'+LOCAL_PORT1.to_bytes(2, 'little'))
time.sleep(0.1)
uart0.write(b'\x57\xab\x15'+bytes(bytearray(TARGET_IP)))
time.sleep(0.1)
uart0.write(b'\x57\xab\x16'+TARGET_PORT.to_bytes(2, 'little'))
time.sleep(0.1)
uart0.write(b'\x57\xab\x21'+BAUD_RATE.to_bytes(4, 'little'))
time.sleep(0.1)
uart0.write(b'\x57\xab\x0D')
time.sleep(0.1)
uart0.write(b'\x57\xab\x0E')
time.sleep(0.1)
uart0.write(b'\x57\xab\x5E')
time.sleep(0.1)
CFG.value(1) #end Config
time.sleep(0.1)
print("config end")


while True:

    while uart0.any() > 0:    
        rxData0 = uart0.read() #reads data from serial
        uart0.write(rxData0)   #Writes the data back to serial
        print(str(rxData0) [2:-1])  #prints data, and removes b' form start and ' from end
        
        
        






