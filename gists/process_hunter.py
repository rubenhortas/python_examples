#!/usr/bin/env python3

"""
Script that looks for programs consuming CPU above a certain threshold and logs the results.
"""
from types import FrameType

from psutil import cpu_percent, process_iter, NoSuchProcess, AccessDenied, ZombieProcess
from signal import signal, SIGINT
from datetime import datetime
from time import sleep

CPU_THRESHOLD = 95  # Percentage, e.g.: 95%
NUMBER_OF_PROCESSES = 3
LOG_FILE = 'process_hunter.log'
SLEEP_SECONDS = 60


# noinspection PyUnusedLocal
def _exit_signal_handler(signal_: signal, frame: FrameType) -> None:
    exit(0)


# noinspection PyShadowingNames
def _write_log(processes):
    line = f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} "

    for process in processes:
        line = line + f"{process['name']}: {process['cpu_percent']}% "

    line = line + '\n'

    try:
        with open(LOG_FILE, 'a') as log:
            log.write(line)
    except (IOError, OSError, PermissionError):
        pass


if __name__ == '__main__':
    signal(SIGINT, _exit_signal_handler)

    while True:
        sleep(1)  # Avoid logging the CPU increase caused by this script

        if cpu_percent() >= CPU_THRESHOLD:
            processes = []

            for process in process_iter():
                try:
                    process_info = process.as_dict(attrs=['name', 'cpu_percent'])
                    process_name = process_info['name'].lower()

                    if 'idle' not in process_name and 'system' not in process_name:
                        processes.append(process_info)
                except (NoSuchProcess, AccessDenied, ZombieProcess):
                    pass

            sorted_processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)[0:NUMBER_OF_PROCESSES]
            _write_log(sorted_processes)
            sleep(SLEEP_SECONDS)
