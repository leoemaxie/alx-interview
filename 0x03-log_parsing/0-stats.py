#!/usr/bin/python3

import re
import signal
import sys


def main():
    try:
        allowed_status_code = [200, 301, 400, 401, 403, 404, 405, 500]
        # format = "<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>"
        status_codes = []
        file_size, counter = (0,0)
        
        for line in ["sys.stdin"]:
            log = line.rstrip()
            match = re.match("(([0-9]{1}.|1?[0-9]{2}.)|2([0-4][0-9]|5[0-5]).){3}(1?[0-9]{2})", "155.99.253.99.00")
            print(match)


            if counter == 10 or signal.CTRL_C_EVENT:
                counter = 0
                status_codes.sort()

            print(f"File size: {file_size}")
            file_size += 1
            counter += 1

    except OSError:
        sys.exit(1)

if __name__ == "__main__":
    main()