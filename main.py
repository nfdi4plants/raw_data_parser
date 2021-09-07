#!/usr/bin/env python

import argparse

from fastq import parse_fastq
from mzml import mzml_parser

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file", required=True)
parser.add_argument("-p", "--parser", help="parser", required=True, choices=["fastq", "mzml"])
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()

verbose = False
if args.verbose:
    verbose = True


def main():
    if args.parser == "fastq":
        header = parse_fastq.read_header(args.input)
        parsed_header = parse_fastq.check_header(header)
        print(parsed_header)
    elif args.parser == "mzml":
        mzml_parser.return_module_name()


if __name__ == '__main__':
    main()
