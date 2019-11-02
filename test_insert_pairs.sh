#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle insert_key_value_pairs.py --ignore=E402
assert_no_stdout
run test_style pycodestyle test_binary_tree.py
assert_no_stdout
run test_style pycodestyle avl.py
assert_no_stdout
run test_style pycodestyle binary_tree.py
assert_no_stdout

run test_bad_number python3 insert_key_value_pairs.py --data_structure hash --dataset rand.txt --data_number 1000000
assert_exit_code 1
run test_bad_file python3 insert_key_value_pairs.py --data_structure hash --dataset aaa.txt --data_number 1000000
assert_exit_code 1
run test_bad_ds python3 insert_key_value_pairs.py --data_structure www --dataset aaa.txt --data_number 1000000
assert_exit_code 1

run test_normal python3 insert_key_value_pairs.py --data_structure hash --dataset rand.txt --data_number 1000
assert_exit_code 0
run test_normal python3 insert_key_value_pairs.py --data_structure AVL --dataset rand.txt --data_number 1000
assert_exit_code 0
run test_normal python3 insert_key_value_pairs.py --data_structure tree --dataset rand.txt --data_number 1000
assert_exit_code 0