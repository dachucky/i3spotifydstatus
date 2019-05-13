#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import subprocess

if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf8')

def get_players():
    try:
        return subprocess.check_output(['playerctl', '-l']).decode('utf-8').splitlines()
    except subprocess.CalledProcessError as err:
        return null

def get_status(player):
    try:
        return subprocess.check_output(['playerctl', '-p', player, 'status']).decode('utf-8') in ['Playing\n']
    except subprocess.CalledProcessError as err:
        return False

def get_playing(player):
    try:
        title = subprocess.check_output(['playerctl', '-p', player, 'metadata', '--format', '{{title}}']).decode('utf-8')[:-1]
        artist = subprocess.check_output(['playerctl', '-p', player, 'metadata', '--format', '{{artist}}']).decode('utf-8')[:-1]
        if artist:
            return artist + ' - ' + title
        else:
            return title
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
        players = get_players()
        j = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        # CHANGE THIS LINE TO INSERT SOMETHING ELSE
        for player in players:
            if get_status(player):
                if player == 'spotify':
                    j.insert(0, {'color' : '#9ec600', 'full_text' : ' %s' % (get_playing(player)) , 'name' : player})
                else:
                    j.insert(0, {'color' : '#00afff', 'full_text' : ' %s' % (get_playing(player)) , 'name' : player})
        # and echo back new encoded json
        print_line(prefix+json.dumps(j))
