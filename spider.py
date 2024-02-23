#!/usr/bin/python3
from urllib.parse import urlparse
import requests

'''url = "https://www.example.com/path/to/resource?query=value#fragment"

# Parsing de l'URL
parsed_url = urlparse(url)

# Affichage des différents composants de l'URL
print("Schéma:", parsed_url.scheme)
print("Netloc:", parsed_url.netloc)
print("Chemin:", parsed_url.path)
print("Query:", parsed_url.query)
print("Fragment:", parsed_url.fragment)'''

COMMAND = "./spider [-rlp] URL\n"
ERR_FIRST_ARG = 'ERROR: First argument should be "./spider"'
ERR_COMMAND_L = 'ERROR: The command should have at list two elements'
command=""
url=""
success=0
flag=("-r", "-l", "-p")

def command_validation(boolean, error_msg):
    global success
    if boolean:
       success=1
    else:
        print(error_msg)
        success=0
    return success

while(not success):
    command = input(COMMAND).split()
    print(command)
    if not command_validation(len(command)>=2, ERR_COMMAND_L): continue
    if not command_validation(command[0]=="./spider", ERR_FIRST_ARG): continue
    print("Success : "+str(success))
    url = command[-1]

    print("URL:"+url)

print(command)
print(f"SUCCESS : {bool(success)}")