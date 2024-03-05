#!/usr/bin/env python3.10

import argparse
import sys
import os
import requests
from bs4 import BeautifulSoup as bs
import re

from pprint import pprint

default_dir = './data/'
default_lim = 5

#I've put default values for L ans P directly inside the parser
def extract_images(limit, path, URL,recursive=False):
    print(recursive, limit, path, URL)
    print("VENV","OK" if os.getenv('VIRTUAL_ENV') else "KO")
    """ headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
    #pprint(headers)
    response = requests.get(url=URL, headers=headers)
    #print('RESPONSE :',response.content)
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        print('SOUP :',soup.prettify())
        imgs = soup.find_all("img")
        if not os.path.exists(path):
            os.makedirs(path)
        count = 0
        urls = [img['src'] for img in imgs]
        for url in urls:
            file = re.search(r'(?i)[^\s]+(\.(jpg|jpeg|png|gif|bmp))$', url)
            if not file:
                print(f'Regeg did nit match withthe url: {url}')
                continue
            #print(file)
            with open(file.group(1), 'wb') as f:
                response = requests.get(f'{URL}{url}')
                f.write(response._content)

    print(imgs) """
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            soup = bs(response.text, 'html.parser')
            imgs = soup.find_all("img")
            if not os.path.exists(path):
                os.makedirs(path)
            count = 0
            for img in imgs:
                src = img.get('src')
                if src:
                    image_url = src if src.startswith('http') else f'{URL}/{src}'
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        file_name = str(count)
                        file_path = os.path.join(path, file_name)
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                        print(f'Successfully downloaded: {file_name}')
                        count += 1
                    else:
                        print(f'Failed to download image from : {image_url}')
                else:
                    print('No src attribute found in img tag')

            
    except Exception as e:
        print('Une erreur s\'est produite :', str(e))        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='./spider', description='The spider program allow you to extract all the images from a website, recursively, by providing a url as a parameter.')
    parser.add_argument("-r", "--recursive", action="store_true",help="recursively downloads the images in a URL received as a parameter")
    parser.add_argument("-l", "--limit", default=default_lim, action="store", help="indicates the maximum depth level of the recursive download otherwise 5")
    parser.add_argument("-p", "--path", default=default_dir, action="store", help="indicates the path where the downloaded files will be saved otherwise './data/'")
    parser.add_argument("URL", help="You must enter the URL from which you want to extract the image here")
    args = parser.parse_args()
    extract_images(args.limit, args.path, args.URL,args.recursive)
