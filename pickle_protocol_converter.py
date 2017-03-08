#!/usr/bin/env python

import pickle
import argparse
import sys
import numpy

def main():
    parser = argparse.ArgumentParser(description='Convert between pickle protocol versions.')
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    parser.add_argument('--version', default=2, type=int, help='The pickle protocol version to write the OUTPUT_FILE.')
    args = parser.parse_args()

    with open(args.input_file, 'rb') as f:
        try:
            data = pickle.load(f)
        except ValueError as e:
            sys.stderr.write(str(e) + "\nPlease use a more recent version of Python to do the conversion.\n")
            sys.exit(1)

    with open(args.output_file, 'wb') as f:
        pickle.dump(data, f, args.version)

    print("Done!")

if __name__ == "__main__": main() 
