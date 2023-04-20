#!python
"""
00. this is a series programs which takes zine pages in the jpg sequence in files\
/ and output a print ready document. Each program does a different format;
0. this one is for 8fold;
1. import and define;
2. clear cache;
3. identify if there are the right amount of jpgs. if there are too many, notifiy\
 the user and continue. if there are not enough make blanks, notify, and continue\
;
4. copy first 8 jpgs to cache;
5. render pdf to PRINT.pdf;
6. clear cache;
7. exit;
"""

#1 Import and define.
import argparse
import logging
import os
import glob
from pyhtml2pdf import converter

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",  action='store_true', help="Increase verbosity.")
args = parser.parse_args()

if args.verbose == True:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
else:
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def gen_blanks(num=1):
    for i in range(0,num):
        logging.warning(f'genorate blank page placeholder function; no functionality!')

def clear_cache():
    cache_files = glob.glob("../cache/*")
    logging.info(f'clearing cach')
    for file in cache_files:
        os.remove(file)

#2 clear cache;
clear_cache()

#3 ideinfy if there are the right amount of jpegs: if there are more then 8, notify the user and continue. If there are not enough, make blanks, notify, and continue.

jpg_files = glob.glob("img*.jpg")
num_jpgs = len(jpg_files)

if num_jpgs > 8:
    logging.warning(f'More than 8 imgs detected. Only first 8 will be used.')

if num_jpgs < 8:
    logging.warning(f'Less than 8 imgs detected. Adding blank pages')
    gen_blanks(8 - num_jpgs)
    jpg_files = glob.glob("img*.jpg")

#4 copy first 8 jpgs to cache

logging.info(f'moving pages to cache')
for i in range(0,8):
    file = jpg_files[i]
    os.system(f"cp {file} ../cache")

cache_files = glob.glob("../cache/*")

#5 render pdf to PRINT.pdf;
html_path = os.path.abspath('../html/8fold.html')
logging.info(f'begining render')
converter.convert(f'file:///{html_path}', 'PRINT.pdf')

#6 clear cache
clear_cache()

#7
exit()
