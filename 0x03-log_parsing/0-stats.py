#!/usr/bin/python3
import sys
from collections import defaultdict
import signal

def print_statistics(total_size, status_counts):
    print(f'Total file size: File size: {total_size}')
    for status_code in sorted(status_counts.keys()):
        print(f'{status_code}: {status_counts[status_code]}')

def signal_handler(sig, frame):
    print_statistics(total_size, status_counts)
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, signal_handler)

line_count = 0
total_size = 0
status_counts = defaultdict(int)

try:
    for line in sys.stdin:
        line_count += 1

        try:
            _, _, _, _, _, status_code, file_size = line.strip().split()
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        total_size += file_size
        status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_statistics(total_size, status_counts)

except KeyboardInterrupt:
    pass

print_statistics(total_size, status_counts)
