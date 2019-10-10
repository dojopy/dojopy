from concurrent.futures import ThreadPoolExecutor, wait
from requests import get
from random import shuffle
def my_query(url):
    return len(get(url).content)

""" 100 urls """
urls = [
    'https://www.google.com',
    'https://www.amazon.com',
    'https://es.aliexpress.com/',
    'https://www.ebay.es/',
    'https://instagram.com',
    'https://www.github.com',
    'https://pastebin.com',
    'https://www.fiverr.com',
    'https://www.mercadolibre.com',
    'https://www.olx.com.pe/',
]*10
shuffle(urls)
print('Number urls: ', len(urls))

""" Not multithreading """
for url in urls:
    my_query(url)




# """ request multithreading"""
# executor = ThreadPoolExecutor(max_workers=len(urls))
# result_querys = [executor.submit(my_query, url) for url in urls]
# wait(result_querys)
