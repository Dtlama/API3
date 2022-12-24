from urllib.parse import urlparse
import os
import requests
from dotenv import load_dotenv
import argparse


def shorten_link(headers, link):
    body = {
      'long_url': link
    }
    response = requests.post('https://api-ssl.bitly.com/v4/shorten', json=body,
                           headers=headers)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(headers, link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'\
        .format(bitlink=link)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(headers, bitlink):
    url = "https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"\
        .format(bitlink=bitlink)
    response = requests.get(url, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()

    token = os.environ["BITLY_API_TOKEN"]

    parser = argparse.ArgumentParser(description='Подсчёт кликов по ссылкам и их сокращение')
    parser.add_argument('link', help='Ваша ссылка: ')
    args = parser.parse_args()
    parser.parse_args()
    link = args.link

    headers = {
      'Authorization': token
    }

    parsed_url = urlparse(link)
    whole_url = f"{parsed_url.netloc}{parsed_url.path}"

    if is_bitlink(headers, whole_url):
        try:
            clicks_count = count_clicks(headers, whole_url)
            print('Количество кликов', clicks_count)
        except requests.exceptions.HTTPError:
            print('Невозможно подсчитать количество кликов')
    else:
        try:
            link_shorten = shorten_link(headers, link)
            print('Битлинк', link_shorten)
        except requests.exceptions.HTTPError:
            print("Ссылка введена неправльно")
