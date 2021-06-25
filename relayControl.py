import RPi.GPIO as GPIO
from pyModbusTCP.client import ModbusClient
import time
from datetime import datetime
import logging
from systemd.journal import JournaldLogHandler



relay = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)


logger = logging.getLogger(__name__)

# instantiate the JournaldLogHandler to hook into systemd
journald_handler = JournaldLogHandler()

# set a formatter to include the level name
journald_handler.setFormatter(logging.Formatter(
    '[%(levelname)s] %(message)s'
))

# add the journald handler to the current logger
logger.addHandler(journald_handler)

# optionally set the logging level
logger.setLevel(logging.DEBUG)


# c = ModbusClient(host="192.168.0.7", auto_open=True, auto_close=True)

# c = ModbusClient()
# c.host("192.168.0.7")
# c.port(502)
# c.unit_id(1)
# # managing TCP sessions with call to c.open()/c.close()

# c.open()

if __name__ == '__main__':

    c = ModbusClient(host="192.168.0.7", auto_open=True, auto_close=True,timeout=0.1)
    c.port(502)
    c.unit_id(1)
    while(1):
        try:
            # print("cetak")
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            regs = c.read_input_registers(0, 2)

            if regs:
                allData = (str(current_time) +" - " + str(regs))

                print(allData)

                logger.info(
            'test log  %s',
            allData
        )

                temp =  regs[0]/100
                rh = regs[1]/100

                if rh<75:
                    GPIO.output(relay, GPIO.HIGH)
                    print("MATI")
                
                else:
                    GPIO.output(relay, GPIO.LOW)
                    print("HIDUP")
            # else:
                # print("read error")

        except:
            print("gagal")

        time.sleep(1)

    # try:

       
    #     regs = c.read_input_registers(0, 2)
    #     if regs:
    #         print(regs)

    #         temp =  regs[0]/100
    #         rh = regs[1]/100

    #         if rh<75:
    #             GPIO.output(relay, GPIO.HIGH)
    #             print("MATI")
            
    #         else:
    #             GPIO.output(relay, GPIO.LOW)
    #             print("HIDUP")



    #     else:
    #         print("read error")
    #         # c.open()

    #     time.sleep(2)
      
    # except:
    #      print("read error excep")
        # c.close()




# while (1):
#     GPIO.output(relay, GPIO.HIGH)
#     time.sleep(2)
#     GPIO.output(relay, GPIO.LOW)
#     time.sleep(2)
    


