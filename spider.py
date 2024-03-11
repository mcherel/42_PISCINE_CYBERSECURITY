#!/usr/bin/env python3.10

import argparse
import sys
import os
import requests
from bs4 import BeautifulSoup as bs
import re
from urllib.parse import urlparse, urljoin

from pprint import pprint

default_dir = './data/'
default_lim = 5
min_img_size = 10000
visited_urls = set()

#I've put default values for L ans P directly inside the parser
def extract_images(limit, path, URL, recursive=False):
    print(recursive, limit, path, URL)
    print("VENV","OK" if os.getenv('VIRTUAL_ENV') else "KO")
    if limit == 0:
        print("The limit has reached a zero")
        exit
    if URL in visited_urls:
        return
    visited_urls.add(URL)
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
        #Session object reuses underlying TCP connection which can lead to better performance
        session = requests.Session()
        response = session.get(URL)
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
                    if not re.search(r'(?i)([^?\s]+)(\.(?:jpg|jpeg|png|gif|bmp))(?:\?|$)', image_url):
                        print(f'Regex did not match within url: {image_url}')
                        continue
                    #print(image_url)
                    response = session.get(image_url, allow_redirects=False)
                    if response.status_code == 200:
                        file_name = str(count)
                        file_path = os.path.join(path, file_name)
                        with open(file_path, 'wb') as f:
                            f.write(response.content)
                        file_size = os.path.getsize(file_path)
                        print("File size : ", file_size,"bytes")
                        # downloading files with min size
                        if file_size > min_img_size:
                            print(f'Successfully downloaded: {file_name}')
                            count += 1
                        else:
                            print(f'Unsuffisiant file size: {file_size}')
                        if count == 5:
                            break

                    else:
                        print(f'Failed to download image from : {image_url}')
                else:
                    print('No src attribute found in img tag')
        if recursive:
            print('LIMIT :'+str(limit))
            limit-=1
            links = soup.find_all('a', href=True)
            top_five_links = links[:10]
            for link in links:
                link_url = urljoin(URL, link['href'])
                #print("LINK : "+str(lnk))
                path+='/_' + str(limit) + "/"
                print("LINK URL:"+link_url)
                #extract_images(limit, path+'/_'+str(limit)+"/", link_url, recursive)
                if limit:
                    extract_images(limit, link_url, link_url, recursive)
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

""" (\.(?:jpg|jpeg|png|gif|bmp))(?:\?|$)':

    r: This denotes a raw string literal in Python, which is often used for regular expressions. It tells Python not to interpret backslashes in any special way, which is useful for regular expressions where backslashes are common.

    (?i): This is a flag that enables case-insensitive matching. The i flag means that the pattern will match regardless of whether the letters are uppercase or lowercase.

    ([^?\s]+): This part of the expression matches one or more characters that are not whitespace (\s) or the question mark (?). Here's what each part means:
        [^?\s]: The [^...] is a negated character class, which matches any character except the ones listed inside the square brackets.
        ?: Matches the literal character "?".
        \s: Matches any whitespace character (space, tab, newline, etc.).
        +: Matches one or more occurrences of the preceding pattern.

    (\.(?:jpg|jpeg|png|gif|bmp)): This part matches a dot followed by one of the specified image file extensions (jpg, jpeg, png, gif, bmp):
        \.: Matches a literal dot (escaped with \ since dot has special meaning in regex).
        (?:jpg|jpeg|png|gif|bmp): This is a non-capturing group ((?:...)) that matches one of the specified image file extensions. It matches either "jpg", "jpeg", "png", "gif", or "bmp".

    (?:\?|$): This part matches either a question mark (\?) or the end of the string ($), but it's a non-capturing group ((?:...)). It's used to ensure that the URL ends either with a question mark (which could indicate query parameters) or at the end of the string. This is to handle cases where the URL may have query parameters appended to it.

So, in summary, this regular expression is designed to match URLs that end with one of the specified image file extensions (jpg, jpeg, png, gif, bmp), and it's case-insensitive. It captures the URL up to the extension while ignoring any query parameters that may be present.
 """