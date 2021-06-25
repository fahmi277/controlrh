import RPi.GPIO as GPIO
from pyModbusTCP.client import ModbusClient
import time

relay = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)

c = ModbusClient()
c.host("192.168.0.7")
c.port(502)
c.unit_id(1)
# managing TCP sessions with call to c.open()/c.close()

c.open()

while(1):
    try:

       
        regs = c.read_input_registers(0, 2)
        if regs:
            print(regs)

            temp =  regs[0]/100
            rh = regs[1]/100

            if rh<75:
                GPIO.output(relay, GPIO.HIGH)
                print("MATI")
            
            else:
                GPIO.output(relay, GPIO.LOW)
                print("HIDUP")



        else:
            print("read error")
            # c.open()

        time.sleep(2)
      
    except:
         print("read error excep")
        # c.close()




# while (1):
#     GPIO.output(relay, GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(relay, GPIO.LOW)
#     time.sleep(2)
    


