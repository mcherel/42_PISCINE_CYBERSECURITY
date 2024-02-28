# 42_PISCINE_CYBERSECURITY
## SPIDER
### Description
The spider program allow you to extract all the images from a website, recursively, by providing a url as a parameter.

Program options:

./spider [-rlp] URL

* Option -r : recursively downloads the images in a URL received as a parameter.
* Option -r -l [N] : indicates the maximum depth level of the recursive download.
If not indicated, it will be 5.
* Option -p [PATH] : indicates the path where the downloaded files will be saved.
If not specified, ./data/ will be used.

The program will download the following extensions by default:

* .jpg/jpeg
* .png
* .gif
* .bm
### REFERENCES
* [open()](https://docs.python.org/fr/3/library/functions.html#open)
* [os.path](https://docs.python.org/fr/3/library/os.path.html#module-os.path)
* [fileinput](https://docs.python.org/fr/3/library/fileinput.html#module-fileinput)
* [OSError](https://docs.python.org/fr/3/library/exceptions.html#OSError)
* [argparse](https://docs.python.org/fr/3/howto/argparse.html)




### A Faire
* posix
* arguments
* fonction download
* Lire
    * os
    * sys
    * requests
    * BeautifulSoup
    * urllib.parse

### Launching Project
    # Create Virtual Environment:

    python -m venv .venv

    # Activate the Virtual Environment:

    source .venv/bin/activate

    # Install Modules

    pip install requests beautifulsoup4

    # Launch python Script

    ./spider [-rlp] URL

    # Quit venv

    deactivate