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

regs = c.read_input_registers(0, 2)
if regs:
    print(regs)
    print(regs[0])
    print(regs[1])
else:
    print("read error")

# while (1):
#     GPIO.output(relay, GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(relay, GPIO.LOW)
#     time.sleep(2)
    


