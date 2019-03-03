#!/usr/bin/python3
import requests
import re
import json
import sys
import os

"""
Requires: Python3.

Usage: python get_imdb_keys.py "url" "output_filename"
where output_filename is on the form imdb_top_250 (exclude .json).

Example: python get_imdb_keys.py "https://www.imdb.com/chart/top?ref_=nv_mv_250" "top_250"
will generate a file top_250.json in /imdb_key_lists/top_250.json.
"""

# Tries to find imdb keys in a list, if that fails tires to find all imdb keys
# instaed. Removes duplicates.
# Writes .json with a list of imdb keys.
def get_imdb_keys_from_url(url, name):
    html_data = requests.get(url).text
    # Search patterns:
    list_specific_pattern = r'"url": "\/title\/(tt[0-9]......)' # matches /title/tt1234567 and puts key in group(1)
    general_pattern = r'\/(tt[0-9]......)'
    # Find keys:
    imdb_key_list = re.findall(list_specific_pattern, html_data)
    if len(imdb_key_list) == 0:
        print('No keys with list structure found, searches for all keys instead...')
        imdb_key_list = re.findall(general_pattern, html_data)
    imdb_key_list = remove_duplicates(imdb_key_list)
    # Make JSON:
    print('IMDb keys found:', len(imdb_key_list))
    if len(imdb_key_list) > 0:
        filename = 'imdb_keys_' + name + '.json'
        make_json(filename, imdb_key_list)

def make_json(filename, imdb_key_list):
    json_string = json.dumps(imdb_key_list)
    os.makedirs(os.path.dirname('imdb_key_lists/' + filename ), exist_ok=True)
    file = open('imdb_key_lists/' + filename, 'w')
    file.write(json_string)
    print('Success! Wrote results to', filename)

def remove_duplicates(key_list):
    return list(set(key_list))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Wrong number of arguments.\nUsage: python get_imdb_keys.py url output_filename')
        exit(0)
    get_imdb_keys_from_url(sys.argv[1], sys.argv[2])
