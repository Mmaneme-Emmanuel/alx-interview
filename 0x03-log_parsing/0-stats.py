#!/usr/bin/python3
"""
Log parsing script
"""

import sys
import signal


def print_stats(log):
    """
    Print the current statistics
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


# Initialize log statistics
log = {
    "file_size": 0,
    "code_frequency": {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0},
}
line_count = 0


def handle_interrupt(signum, frame):
    """
    Handle keyboard interruption to print stats before exiting
    """
    print_stats(log)
    sys.exit(0)


# Register signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        try:
            # Parse log line
            parts = line.strip().split()
            if len(parts) < 9:
                continue

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            log["file_size"] += file_size

            # Update status code frequency
            if status_code in log["code_frequency"]:
                log["code_frequency"][status_code] += 1

            # Increment line count
            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(log)

        except Exception:
            # Ignore lines that cannot be parsed
            continue

finally:
    # Print final stats when exiting
    print_stats(log)
