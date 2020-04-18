import requests, os, sys

file_path = os.path.join(sys.path[0], 'quotes.txt')
log_file = open(file_path, 'a')

quote = requests.get('https://ron-swanson-quotes.herokuapp.com/v2/quotes')
quote = quote.json()
quote = quote[0]

log_file.write(f'{quote}\n')
log_file.close()
