#!/usr/bin/python3
'''Module 1-mylist.py'''


class MyList(list):
    '''
    A class that inherits from list
    '''

    def print_sorted(self):
        '''
        prints the sorted list
        '''
        print(sorted(self))
