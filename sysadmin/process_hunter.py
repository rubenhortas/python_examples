#!/usr/bin/env python3

from psutil import cpu_percent, process_iter, NoSuchProcess, AccessDenied, ZombieProcess
from signal import signal, SIGINT
from datetime import datetime
from time import sleep

"""
This script looks for programs consuming CPU above a certain threshold and logs the results.
"""

CPU_THRESHOLD = 95  # Percentage, ex: 95%
NUMBER_OF_PROCESSES = 3
LOG_FILE = 'process_hunter.log'
SLEEP_SECONDS = 60


# noinspection PyUnusedLocal
def exit_signal_handler(signal_, frame):
    exit(0)


def main():
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
            write_log(sorted_processes)
            sleep(SLEEP_SECONDS)


def write_log(processes):
    log_line = f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} "

    for process in processes:
        log_line = log_line + f"{process['name']}: {process['cpu_percent']}% "

    log_line = log_line + '\n'

    try:
        with open(LOG_FILE, 'a') as log:
            log.write(log_line)
    except (IOError, OSError, PermissionError):
        pass


if __name__ == '__main__':
    signal(SIGINT, exit_signal_handler)
    main()
