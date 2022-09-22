#!/usr/bin/python3
''' function to find the largest of an input list
'''


def find_peak(list_of_integers):
    if list_of_integers:
        return max(set(list_of_integers))
    return
