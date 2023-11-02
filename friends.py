import os
import sys
import MySQLdb


class Friend:
    ID = 0
    Name = ''
    URL = ''


def get_list():
    friend_list = []

    friend = Friend()
    friend.ID = 1
    friend.Name = '欧雷'
    friend.URL = 'https://ourai.ws/'

    friend_list.append(friend)
    return friend_list
