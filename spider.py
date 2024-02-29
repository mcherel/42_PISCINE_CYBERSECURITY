#!/usr/bin/env python3.10

import argparse
import sys

def extract_images(recursive, limit, path, url):
    print(recursive, limit, path, url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='./spider', description='The spider program allow you to extract all the images from a website, recursively, by providing a url as a parameter.')
    parser.add_argument("-r", "--recursive", action="store_true",help="recursively downloads the images in a URL received as a parameter")
    parser.add_argument("-l", "--limit", type=int, default=5, action="store", help="indicates the maximum depth level of the recursive download otherwise 5")
    parser.add_argument("-p", "--path", default='./data/', action="store", help="indicates the path where the downloaded files will be saved otherwise './data/'")
    parser.add_argument("url", help="You must enter the URL from which you want to extract the image here")
    args = parser.parse_args()
    extract_images(args.recursive, args.limit, args.path, args.url)
