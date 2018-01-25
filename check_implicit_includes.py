#!/bin/python

import re
import glob
import os
import sys
from pprint import pprint


def get_filename_from_include(include):
    m = re.search('(".*")|(<.*>)', include)
    return m.group(0)[1:-1]

def read_headers(filename):
    with open(filename, "r") as source:
        return set([
            get_filename_from_include(line)
            for line in source
            if line.startswith("#include")
        ])

def find_header_file(filename, directory):
    pattern = "{}/**/{}".format(directory, filename)
    return glob.glob(pattern, recursive=True)



if __name__ == "__main__":
    source = sys.argv[1]
    source_headers = read_headers(source)

    subheaders = set()
    for index, header in enumerate(source_headers):
        print("processing header {}. Progress {}/{}".format(header, index, len(source_headers)))
        path = find_header_file(header, ".")

        if len(path) == 0:
            print("no files found, skipping...")
            continue

        if len(path) > 1:
            print("more than one file found, skipping...")
            continue

        subheaders = subheaders.union(read_headers(path[0]))

    print("EXPLICIT AND IMPLICIT HEADERS")
    print("-----------------------------")
    pprint(source_headers.intersection(subheaders))
