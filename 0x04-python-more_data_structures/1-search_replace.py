#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = []
    for ele in my_list:
        if ele == search:
            ele = replace
        new_list.append(ele)
    return new_list
