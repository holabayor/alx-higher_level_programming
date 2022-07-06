#!/usr/bin/python3
""" Script that adds all arguments to a Pyhton list
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

items = []
items.extend(sys.argv[1:])
filename = "add_item.json"
save_to_json_file(items, filename)
load_from_json_file(filename)
