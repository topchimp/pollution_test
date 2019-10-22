from sds011 import *
import sys, io, datetime
sys.path.append("/usr/local/lib/python3.7/site-packages")
import serial
#sensor = SDS011("/dev/cu.wchusbserial1430")
sensor = SDS011("/dev/cu.usbserial-1430")
# Turn-on sensor
# sensor.sleep(sleep=False)
time.sleep(10)
f = open("readings.txt", "a", encoding="utf-8")
while(True):
  pmt_2_5, pmt_10 = sensor.request()
  # print (time_now(), end='')
  # print(f"PMT25: {pmt_2_5} microg/m3  ", end='')
  # print(f"MPT10 : {pmt_10} microg/m3")
  # Turn-off sensor
  # sensor.sleep(sleep=True)
  # time.sleep(2)
  f.write(f"{datetime.datetime.now()},{pmt_2_5},{pmt_10}\n")
  f.flush()
  time.sleep(20)
