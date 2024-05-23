#!/usr/bin/env python3
import os
import stat
import time
import sys
import argparse

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

def list_directory_details(path='.', sort_by='size'):
    os.system('cls' if os.name == 'nt' else 'clear')
    entries = os.listdir(path)
    details = [(entry, os.stat(os.path.join(path, entry))) for entry in entries]

    # Sorting logic based on command line argument
    if sort_by == 'size':
        details.sort(key=lambda x: x[1].st_size, reverse=True)
    elif sort_by == 'name':
        details.sort(key=lambda x: x[0].lower())
    elif sort_by == 'lastedited':
        details.sort(key=lambda x: x[1].st_mtime, reverse=True)

    print(f"{'Permissions':>10} {'Links':>5} {'UID':>5} {'GID':>5} {'Size':>10} {'Modified':>12} {'Name'}")
    print("-" * 79)

    for entry, stats in details:
        permissions = stat.filemode(stats.st_mode)
        n_links = stats.st_nlink
        uid = stats.st_uid
        gid = stats.st_gid
        size = human_readable_size(stats.st_size)
        mtime = time.strftime("%b %d %H:%M", time.localtime(stats.st_mtime))
        print(f"{permissions:>10} {n_links:>5} {uid:>5} {gid:>5} {size:>10} {mtime:>12} {entry}")

def continuously_list_details(path='.', interval=5, sort_by='size'):
    try:
        while True:
            list_directory_details(path, sort_by)
            time.sleep(interval)
    except KeyboardInterrupt:
        pass

def main():
    parser = argparse.ArgumentParser(description="List directory contents sorted by size, name, or last edited time. It refreshes the screen with updated contents every 5 seconds")
    parser.add_argument('path', type=str, help="Directory path to list")
    parser.add_argument('--size', '-s', action='store_const', const='size', dest='sort_by', help="Sort by file size")
    parser.add_argument('--name', '-n', action='store_const', const='name', dest='sort_by', help="Sort by file name")
    parser.add_argument('--lastedited', '-e', action='store_const', const='lastedited', dest='sort_by', help="Sort by last edited time")
    parser.set_defaults(sort_by='size')  # Default sort is by size

    args = parser.parse_args()

    continuously_list_details(args.path, 5, args.sort_by)

if __name__ == "__main__":
    main()
