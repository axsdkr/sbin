#!/usr/bin/env python3

import argparse
import glob
import os
import random
import string


def generate_random_name(length):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def rename_file(current_name, new_name):
    os.rename(current_name, new_name)


def main():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options] <file>",
        description="renaming files with random names",
    )

    parser.add_argument(
        "current_name",
        nargs="*",
        type=str,
        help="current name of the file(s)",
        metavar="<file>",
    )
    parser.add_argument(
        "-l",
        "--length",
        default=20,
        type=int,
        help="length of the random name (default: 20)",
    )

    args = parser.parse_args()
    files = []

    if not args.current_name:
        parser.print_help()
    else:
        for pattern in args.current_name:
            files.extend(glob.glob(pattern))

    for current_name in files:
        if os.path.isfile(current_name):
            file_extension = os.path.splitext(current_name)[1]
            new_name = generate_random_name(args.length) + file_extension
            rename_file(current_name, new_name)


if __name__ == "__main__":
    main()
