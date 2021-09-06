#!/usr/bin/env python

import argparse

from fastq import fastq_parser
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
        fastq_parser.return_module_name()
    elif args.parser == "mzml":
        mzml_parser.return_module_name()

if __name__ == '__main__':
    main()
