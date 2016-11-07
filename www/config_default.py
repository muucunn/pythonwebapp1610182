#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '',
        'db': 'test'
    },
    'session': {
        'secret': 'Awesome'
    }
}

'''
 password='www'改为：password=''  ，user='www'改为：user='root' 
    #db='awesome'改为db='test'  201611071041
'''
