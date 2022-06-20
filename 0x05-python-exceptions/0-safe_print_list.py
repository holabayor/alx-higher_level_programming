
#!/usr/bin/python3
""" Function that prints x elements of a list"""
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end=" ")
    except:
        raise Exception
    return x+1
