#!py -3
"""
Author : Linnea Honeker
Date   : 2020-04-13
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crows Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.positional

    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
