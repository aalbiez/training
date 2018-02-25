# -*- coding: utf-8 -*-

import psutil
import time
from datetime import datetime

programs = ['0ad', 'evince']

track = {
    '0ad': 0,
    'evince': 0,
}


def list_monitored_processes():
    for proc in psutil.process_iter():
         try:
             pinfo = proc.as_dict(attrs=['name'])
             if pinfo['name'] in programs:
                 yield pinfo['name']
         except psutil.NoSuchProcess:
             pass

while True:
    time.sleep(5)
    print datetime.now().isoformat(), 5, list(list_monitored_processes())
