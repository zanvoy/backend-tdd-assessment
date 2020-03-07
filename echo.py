#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Perform transformation on input text.')
    parser.add_argument('-u', '--upper', action='store_true', help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true', help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true',  help='convert text to titlecase')
    parser.add_argument('text', help='text to be manipulated')
    return parser

def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)

    output = ns.text
    if ns.upper == True:
        output = output.upper()
    if ns.lower == True:
        output = output.lower()
    if ns.title == True:
        output = output.title()
    return output


if __name__ == '__main__':
    main(sys.argv[1:])
