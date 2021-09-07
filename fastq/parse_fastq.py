#!/usr/bin/env python

import gzip
import re
from collections import OrderedDict


rx_pattern = r"@(?P<instrument>[a-zA-Z0-9-_]+):" \
             r"(?P<run_number>[0-9]+):" \
             r"(?P<flowcell_ID>[a-zA-Z0-9]+):" \
             r"(?P<lane>[0-9]+):" \
             r"(?P<tile>[0-9]+):" \
             r"(?P<xpos>[0-9]+):" \
             r"(?P<ypos>[0-9]+):?" \
             r"(?P<umi>[ACGTN+]*) " \
             r"(?P<read>[12]):" \
             r"(?P<is_filtered>[YN]):" \
             r"(?P<control_number>[0-9]+):" \
             r"(?P<index>[ACGTN])"


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

    if rx_match:
        return rx_match.groupdict()
    else:
        return None
