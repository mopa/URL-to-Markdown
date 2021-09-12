#!/usr/bin/env python
# coding: utf-8
#

import requests
from bs4 import BeautifulSoup
import pyperclip
import sys


######################################
# HEADER
#
headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

# Regular Season
page = sys.argv[1]


pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')



######################################
# SCRAP TITLE 
#
title = pageSoup.find('title')

titleMD = '[' + title.text + ']' + '(' + page + ')'
pyperclip.copy(titleMD)


# Sacamos por pantalla el resultado
print("")
print("")
print("Se ha copiado el siguiente texto al portapapeles: ")
print(titleMD)
