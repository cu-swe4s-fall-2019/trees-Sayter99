import binary_tree
import os
import sys
import argparse
import time
import avl
sys.path.append('hash_table')
from hash_table import hash_functions
from hash_table import hash_tables


# parse arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='The right way to pass parameters.',
        prog='insert_key_value_pairs.py')

    # require data structure type
    parser.add_argument('--data_structure',
                        type=str,
                        help='Specify a data structure to use',
                        required=True)

    # require input dataset
    parser.add_argument('--dataset',
                        type=str,
                        help='The file name of the dataset',
                        required=True)

    # require number of data
    parser.add_argument('--data_number',
                        type=int,
                        help='How many key/value pairs to use',
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if (args.data_number >= 10000):
        print('Too large data number')
        sys.exit(1)
    elif (args.data_number < 10):
        print('Too small data number')
        sys.exit(1)

    if not os.path.exists(args.dataset):
        print('Cannot find dataset')
        sys.exit(1)
    else:
        index = 0
        # key/value pairs are key/key_val here
        if (args.data_structure == 'hash'):
            # create hash table with N = 1000000
            # add, search
            container = hash_tables.ChainedHash(1000000,
                                                hash_functions.h_rolling)
            start = time.time()
            keys = []
            for l in open(args.dataset):
                keys.append(l)
                if (index < args.data_number):
                    container.add(l, l + '_val')
                index = index + 1
            end = time.time()
            print('insert: ' + str(end - start))
            sys.exit(0)
        elif (args.data_structure == 'AVL'):
            # insert, search
            container = avl.AVL()
            start = time.time()
            keys = []
            for l in open(args.dataset):
                keys.append(l)
                if (index < args.data_number):
                    container.insert(l, l + '_val')
                index = index + 1
            end = time.time()
            print('insert: ' + str(end - start))
            sys.exit(0)
        elif (args.data_structure == 'tree'):
            # insert, search
            container = binary_tree.BinaryTree()
            start = time.time()
            keys = []
            for l in open(args.dataset):
                keys.append(l)
                if (index < args.data_number):
                    container.insert(l, l + '_val')
                index = index + 1
            end = time.time()
            print('insert: ' + str(end - start))
            sys.exit(0)
        else:
            print('Invalid data structure')
            sys.exit(1)
