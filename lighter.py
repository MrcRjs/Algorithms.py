#!/usr/bin/env python3
# coding: utf-8

import os
import re
import dbus
import time
from backlight import set_backlight
from sys import argv

def backlightController(deb):
  while True:
    try:
      dev = os.open("/sys/devices/platform/applesmc.768/light", os.O_RDONLY)
      lightStr = str(os.read(dev,16))
      lightValue = int(re.search(r'\((\d{1,3}),', lightStr).group(1))
      if deb:
        print("Light Sensor:", lightValue)
      if lightValue <= 4 :
        if lightValue <= 2:
          set_backlight(255)
        else:
          set_backlight(128)
      else:
        set_backlight(0)
      time.sleep(3)
    except EOFError:
      break

if __name__ == '__main__':
    if len(argv[1:]) == 0:
        backlightController(False)
    if len(argv[1:]) == 1:
        if argv[1] == "--debug" or argv[1] == "-d":
            # ./lighter.py (-d|--debug)
            backlightController(True)
        else:
            print("Unknown argument:", argv[1])
    elif len(argv[1:]) > 1:
      print("Script takes 0 or 1 arguments.", len(argv[1:]), "arguments provided.")
