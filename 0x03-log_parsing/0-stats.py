#!/usr/bin/python3
"""
Log parsing script
"""

import sys
import re


def output(log: dict) -> None:
    """
    Helper function to display statistics.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    # Regular expression to match input format
    regex = re.compile(
        r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1

                # Extract fields
                status_code = match.group(3)
                file_size = int(match.group(4))

                # Update metrics
                log["file_size"] += file_size
                if status_code in log["code_frequency"]:
                    log["code_frequency"][status_code] += 1

                # Output after every 10 lines
                if line_count % 10 == 0:
                    output(log)

    except KeyboardInterrupt:
        pass
    finally:
        # Final output
        output(log)
