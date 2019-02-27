#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'https://www.imdb.com/title/tt2663632/'
data = requests.get(url).text
print(data.encode('utf8'))
