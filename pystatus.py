#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import subprocess

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')

def get_status():
    try:
        return subprocess.check_output(['playerctl', '-p', 'spotify', 'status']).decode('utf-8') in ['Playing\n']
    except subprocess.CalledProcessError as err:
        return False

def get_playing():
    try:
        return subprocess.check_output(['playerctl', '-p', 'spotify', 'metadata', '--format', '{{artist}} - {{title}}']).decode('utf-8')[:-1]
    except subprocess.CalledProcessError as err:
        return

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def get_governor():
    with open('/sys/devices/platform/i5k_amb.0/temp4_input') as fp:
        return fp.readlines()[0].strip()

if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:

        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','
        if get_status():
            j = json.loads(line)
            # insert information into the start of the json, but could be anywhere
            # CHANGE THIS LINE TO INSERT SOMETHING ELSE
            j.insert(0, {'color' : '#9ec600', 'full_text' : ' %s' % (get_playing()) , 'name' : 'spotify'})
            # and echo back new encoded json
            print_line(prefix+json.dumps(j))
        else:
            j = json.loads(line)
            print_line(prefix+json.dumps(j))
            #print_line(json.dumps(j))
