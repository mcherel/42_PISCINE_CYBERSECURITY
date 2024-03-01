#!/usr/bin/env python3.10

import argparse
import sys
import os
import requests
from bs4 import BeautifulSoup as bs

from pprint import pprint

def extract_images(recursive, limit, path, URL):
    print(recursive, limit, path, URL)
    print("VENV","OK" if os.getenv('VIRTUAL_ENV') else "KO")
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
    response = requests.get(url=URL, headers=headers)
    print('RESPONSE :',response.content)
    pprint(headers)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='./spider', description='The spider program allow you to extract all the images from a website, recursively, by providing a url as a parameter.')
    parser.add_argument("-r", "--recursive", action="store_true",help="recursively downloads the images in a URL received as a parameter")
    parser.add_argument("-l", "--limit", default=5, action="store", help="indicates the maximum depth level of the recursive download otherwise 5")
    parser.add_argument("-p", "--path", default='./data/', action="store", help="indicates the path where the downloaded files will be saved otherwise './data/'")
    parser.add_argument("URL", help="You must enter the URL from which you want to extract the image here")
    args = parser.parse_args()
    extract_images(args.recursive, args.limit, args.path, args.URL)
