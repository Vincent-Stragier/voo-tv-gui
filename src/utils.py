""" This module contains all the useful functions of this project. """
import os
import re
import sys
from functools import reduce

# Files and directories related functions


def list_files(path: str):
    """List all the files in a folder and subfolders.

    Args:
        path: the path to use as parent directory.
    Returns:
        A list of files.
    """
    files_list = set()

    for folder, _, files in os.walk(path):
        for file_ in files:
            files_list.add(os.path.join(folder, file_))

    return list(files_list)


def ensure_path(path: str):
    """ Ensure the existence of a specified path.

    Args:
        path: path to create if non existing.
    """
    if not os.path.isdir(path):
        os.makedirs(path)


def find_files(basename_prefix: str, sources: dict):
    """Find the path to the file if it exists.

    Args:
        basename_prefix: the basename prefix of the recording.
        sources: the sources to use.
    Returns:
        An empty list or a list of string which contains the path to the files.
    """
    for files in sources.values():
        matching_files = [
            file_ for file_ in files
            if os.path.basename(file_).startswith(basename_prefix + '_')
        ]

        if matching_files:
            return matching_files
    return []


# Args parsing related functions
def display_arguments(args, message: str = ''):
    """ Display the parsed arguments. """
    if message is not None and message == '':
        print('The following arguments have been parsed:')
    elif message is not None and message != '':
        print(message)

    for key, value in vars(args).items():
        print('{0}: {1}'.format(key, value))


def handle_yes_no(args):
    """ Handle the arguments 'yes' and 'no'. """
    if not args.no:
        print()
        if not args.yes:
            try:
                while True:
                    conti = input('Do you want to run the program (yes/no)? ')
                    if conti.lower() in ('n', 'no'):
                        sys.exit()

                    elif conti.lower() in ('y', 'yes'):
                        break

            except KeyboardInterrupt:
                print(
                    '\nThe user requested the end of the program'
                    ' (KeyboardInterrupt).',
                )

                sys.exit()
    else:
        sys.exit()


# String processing related function
def split_keep_sep(string, separator):
    """Split a string according to a separator.

    Args:
        string: the string to split.
        separator: the separator to use and to keep.

    Returns:
        A list with the spliced elements.
    """
    return reduce(
        lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == separator
        else acc + [elem], re.split('(%s)' % re.escape(separator), string), [],
    )


# PyInstaller related function
def resource_path(relative_path: str):
    """Get absolute path to resource, works for dev and for PyInstaller.

    Args:
        relative_path: the path to resolve.

    Returns:
        The absolute path to the ressource.
    """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)),
    )

    return os.path.join(base_path, relative_path)


def command_to_key(command: str, protocol: str = 'rfb'):
    """Convert a command to a key.

    Args:
        command: the command to convert.

    Returns:
        The key corresponding to the command.
    """
    try:
        return {
            'power_off': {'rfb': 57344, 'http': 409},
            'stop': {'rfb': 58370, 'http': 413},
            'play_pause': {'rfb': 58368, 'http': 179},
            'fast_forward': {'rfb': 58373, 'http': 417},
            'fast_reverse': {'rfb': 58375, 'http': 412},
            'volume_up': {'rfb': 57347, 'http': 447},
            'volume_down': {'rfb': 57348, 'http': 448},
            'mute': {'rfb': 57349, 'http': 449},
            'home': {'rfb': 61184, 'http': 36},
            'info': {'rfb': 57358, 'http': 457},
            'left': {'rfb': 57602, 'http': 37},
            'right': {'rfb': 57603, 'http': 39},
            'up': {'rfb': 57600, 'http': 38},
            'down': {'rfb': 57601, 'http': 40},
            'red_key': {'rfb': 57856, 'http': 45},
            '0': {'rfb': 58112, 'http': 48},
            '1': {'rfb': 58113, 'http': 49},
            '2': {'rfb': 58114, 'http': 50},
            '3': {'rfb': 58115, 'http': 51},
            '4': {'rfb': 58116, 'http': 52},
            '5': {'rfb': 58117, 'http': 53},
            '6': {'rfb': 58118, 'http': 54},
            '7': {'rfb': 58119, 'http': 55},
            '8': {'rfb': 58120, 'http': 56},
            '9': {'rfb': 58121, 'http': 57},
            'be_tv': {'rfb': 57359, 'http': 602},
            'record': {'rfb': 58371, 'http': 416},
            'vod': {'rfb': 61224, 'http': 605},
            'tv': {'rfb': 57360, 'http': 622},
            'ok': {'rfb': 57345, 'http': 10},
            'back': {'rfb': 57346, 'http': 608},
            'guide': {'rfb': 57355, 'http': 458},
        }[command][protocol]
    except KeyError:
        return f'"{command}" is not a valid command'


if __name__ == '__main__':
    print('utils.py is a module, not a script')
