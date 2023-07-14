#!/usr/bin/python3
import sys


def print_status():
    '''
    Prints the status of the requests
    and file size based on input from stdin.
    '''

    counter = 0
    total_size = 0
    file_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    for line in sys.stdin:
        data = line.split()
        try:
            size = int(data[-1])
            code = data[-2]
            total_size += size
            status_codes[code] += 1
        except:
            continue

        if counter == 9:
            print("Total File size: {}".format(total_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            counter = 0
        counter += 1

    if counter < 9:
        print("Total File size: {}".format(total_size))
        for key, value in sorted(status_codes.items()):
            if value != 0:
                print("{}: {}".format(key, value))


if __name__ == "__main__":
    print_status()
