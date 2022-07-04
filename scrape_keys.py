#!/usr/bin/env python3
# Scrape key codes

from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = 'https://docs.qmk.fm/#/keycodes_basic'
driver = webdriver.Remote(
    command_executor='http://192.168.0.209:4444/wd/hub',
    options=webdriver.FirefoxOptions()
)


def main():
    driver.get(url)
    soup = bs(driver.page_source, 'html.parser')

    article = soup.find(attrs={'id': 'main'})
    headers = [h.text for h in article.find_all('h2')]
    tables = article.find_all('tbody')

    output = {}
    for title, table in zip(headers, tables):
        output[title] = []
        for row in table.find_all('tr'):
            data = [d.text for d in row.find_all('td')]
            key = data.pop(0)
            desc = data.pop(-1)
            aliases = data[0].split(',') if data else data

            if ' and ' in desc:
                disp = desc.split(' and ')[0].upper()
            elif len(desc) < 7:
                disp = desc
            else:
                disp = ''

            output[title].append({
                'key': key,
                'desc': desc,
                'aliases': aliases,
                'display': disp
            })

    print(output)


if __name__ == '__main__':
    main()
