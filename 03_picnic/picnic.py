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
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='list',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true',
                        default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sort_arg = args.sorted
    items_arg = args.positional

    if sort_arg == True:
        items_arg.sort()
    

    if len(items_arg) == 1:
        str_items = items_arg
        print ('You are bringing {}'.format(str_items))
    else:
        sec_item = items_arg.pop()
        joined_items = ', '.join(items_arg)
        print ('You are bringing {} and {}'.format(joined_items, sec_item))
    #else:
    #    last_item = items_arg.pop()
    #    print ('You are bringing {} and {}'.format(items_arg, last_item))

        
# --------------------------------------------------
if __name__ == '__main__':
    main()
