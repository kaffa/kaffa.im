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
    friend.Name = '欧雷流'
    friend.URL = 'https://ourai.ws/'
    friend.Intro = "我叫欧雷，是一个出生于上世纪 80 年代的理想主义叛逆青年。喜欢日本，热爱咖啡，善于总结。这里有我对技术和语言的研究，也有对世界和生活的思考。"
    friend.Owner = '欧雷'
    friend.Icon = 'https://ourai.ws/assets/avatars/ourai-100px-3bcaa1cb0c7fa0547d15622572d74a8bbc98a5f62e4920ecddb72ca95e505d17.jpg'

    friend_list.append(friend)
    return friend_list
