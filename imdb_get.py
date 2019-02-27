import requests
import re
import json

def get_imdb_keys_from_imdb_list(url, genre):
    data = requests.get(url).text
    imdb_key_list = re.findall(r'"url": "\/title\/(tt[0-9]......)', data)
    print('imdb keys found:', len(imdb_key_list))
    filename = 'imdb_keys_' + genre + '_' + url[26:37] + '.json'    # WARNING: hardcoded name, might fail if listname is not on index url[26:37]
    make_json(filename, imdb_key_list)

def make_json(filename, imdb_key_list):
    json_string = json.dumps(imdb_key_list)
    file = open(filename, 'w')
    file.write(json_string)
    print('Wrote results to', filename)

# useful lists: https://www.imdb.com/list/ls057823854/

fantasy_list_url = 'https://www.imdb.com/list/ls051689462/'
drama_list_url = 'https://www.imdb.com/list/ls051689627/'

get_imdb_keys_from_imdb_list(drama_list_url, 'drama')
