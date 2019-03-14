#!/usr/bin/env python3

import argparse
import os


# --- Arguments ---
argument_parser = argparse.ArgumentParser(description="Find all empty sub folders of a folder. Ignore folders named `.git` or `DerivedData`.")

# Project folder argument
argument_parser.add_argument('path', help='Path of the folder containing your `.xcodeproj` folder.')

# Ignore folders argument
argument_parser.add_argument('-i', '--ignore-dir',
                             action='append',
                             dest='ignored_folders',
                             metavar='<dirpath>',
                             help='Path of a folder to ignore.')


# --- Parse arguments ---
args = argument_parser.parse_args()

# Folder to ignore given as argument
arged_ignored_folders = set(args.ignored_folders or [])
ignored_folders = set()
for folder in arged_ignored_folders:
    while folder and folder[-1] == os.path.sep:
        folder = folder[:-1]
    ignored_folders.add(folder)

# Forced folders to ignore
ignored_folders = {
    'DerivedData',
    '.git',
} | ignored_folders

# Remove ending slashes to path
path = args.path
while path and path[-1] == os.path.sep:
    path = path[:-1]

# Walk to find empty folders
for (dirpath, dirnames, filenames) in os.walk(path):
    relative_dirpath = dirpath[len(path):]

    # Filter folders to ignore
    folder_parts = set(relative_dirpath.split(os.path.sep))
    if ignored_folders & folder_parts:
        continue
        
    if not dirnames and not filenames:
        print(relative_dirpath)
