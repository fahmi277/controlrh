import RPi.GPIO as GPIO
from pyModbusTCP.client import ModbusClient
import time

relay = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)


# c = ModbusClient(host="192.168.0.7", auto_open=True, auto_close=True)
SERVER_HOST = "192.168.0.7"
SERVER_PORT = 502
c = ModbusClient()
c.host(SERVER_HOST)
c.port(SERVER_PORT)
c.port(502)
c.unit_id(1)
# managing TCP sessions with call to c.open()/c.close()

# c.open()

while True:
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, read register (modbus function 0x03)
    if c.is_open():
        # read 10 registers at address 0, store result in regs list
        regs = c.read_input_registers(0, 2)
        # if success display registers
        if regs:
            print("reg ad #0 to 9: "+str(regs))

    # sleep 2s before next polling
    time.sleep(2)

# while(1):
#     try:

       
#         regs = c.read_input_registers(0, 2)
#         if regs:
#             print(regs)

#             temp =  regs[0]/100
#             rh = regs[1]/100

#             if rh<75:
#                 GPIO.output(relay, GPIO.HIGH)
#                 print("MATI")
            
#             else:
#                 GPIO.output(relay, GPIO.LOW)
#                 print("HIDUP")



#         else:
#             print("read error")
#             # c.open()

#         time.sleep(2)
      
#     except:
#          print("read error excep")
        # c.close()




# while (1):
#     GPIO.output(relay, GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(relay, GPIO.LOW)
#     time.sleep(2)
    


