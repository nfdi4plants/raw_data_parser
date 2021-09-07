#!/usr/bin/env python

import gzip
import re


rx_pattern = r"@([a-zA-Z0-9-_]+):([0-9]+):([a-zA-Z0-9]+):([0-9]+):([0-9]+):([0-9]+):([0-9]+):?([ACGTN+]*) ([12]):([YN]):([0-9]+):([ACGTN])"


def return_module_name():
    print("fastq_parser module loaded")


def read_header(filename):
    try:
        with gzip.open(filename, "rt") as f:
            return f.readline()
    except gzip.BadGzipFile:
        with open(filename) as f:
            return f.readline()


def check_header(header):
    rx_match = re.match(rx_pattern, header)

    if not rx_match:
        return None
    elif len(rx_match.groups()) == 12:
        return {
            "instrument": rx_match.group(1),
            "run_number": rx_match.group(2),
            "flowcell_ID": rx_match.group(3),
            "lane": rx_match.group(4),
            "tile": rx_match.group(5),
            "xpos": rx_match.group(6),
            "ypos": rx_match.group(7),
            "umi": rx_match.group(8),
            "read": rx_match.group(9),
            "is_filtered": rx_match.group(10),
            "control_number": rx_match.group(11),
            "sample_number": rx_match.group(12)
        }
    elif len(rx_match.groups()) == 11:
        return {
            "instrument": rx_match.group(1),
            "run_number": rx_match.group(2),
            "flowcell_ID": rx_match.group(3),
            "lane": rx_match.group(4),
            "tile": rx_match.group(5),
            "xpos": rx_match.group(6),
            "ypos": rx_match.group(7),
            "read": rx_match.group(8),
            "is_filtered": rx_match.group(9),
            "control_number": rx_match.group(10),
            "sample_number": rx_match.group(11)
        }
    else:
        raise ValueError("ERROR: Check RegEx and header, it should return 12 fields.\n" + rx_match.groups())
