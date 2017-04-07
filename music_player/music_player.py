'''
Checks the songs available locally
Creates playlists based on popular online playlists
'''

import os
import sys
import subprocess
from glob import glob


def get_dir():
    directory_path = os.path.dirname(os.path.realpath(__file__))
    print 'Directory : {}\nFiles:'.format(directory_path)
    return directory_path


def make_playlist(directory_path):
    r1 = [y for x in os.walk(directory_path) for y in glob(os.path.join(x[0], '*.mp3'))]
    r2 = [y for x in os.walk(directory_path) for y in glob(os.path.join(x[0], '*.wav'))]
    result = r1 + r2
    return result


def write_playlist_to_file(result, dir_len):
    with open("playlist.m3u", "w") as w:
        for i in result:
            print ".{}".format(i[dir_len:])
            w.write('{0}\n'.format(i))


def play_playlist():
    if sys.platform.startswith('linux'):
        subprocess.call(["xdg-open", 'playlist.m3u'])

if __name__ == '__main__':
    directory_path = get_dir()
    result = make_playlist(directory_path)
    dir_len = len(directory_path)
    write_playlist_to_file(result, dir_len)
    play_playlist()
