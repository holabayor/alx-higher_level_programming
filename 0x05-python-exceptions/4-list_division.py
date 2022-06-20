#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list1[i] / my_list2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            result.append(div)
    return result
