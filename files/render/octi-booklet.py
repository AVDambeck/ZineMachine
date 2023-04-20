#!python
"""
00. this is a series programs which takes zine pages in the jpg sequence in files\
/ and output a print ready document. Each program does a different format;
0. this one is for octi-booklet;
1. import and define;
2. clear cache;
3. identify if there are the number of jpgs is a multipule of four. if there is less than four, abort. If there is a multipule of four, continue. If -f is specified, add blanks. otherwise abort;
4. unless --nocover is specified, modify the jpg_files list: move 2nd image to the end;
5. copy 2 jpgs to cache: the first and last, then second and second to last...;
6. render pdf to cache;
7. repeat 5 & 6 until all pages have been processed.
8. combine the cached pdfs to PRINT.pdf.
9. clear cache;
10. exit;
"""

#1 Import and define.
import argparse
import logging
import os
import glob
from pyhtml2pdf import converter

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",  action='store_true', help="Increase verbosity.")
parser.add_argument("-f", "--force",  action='store_true', help="Avoid aborting. Will add blank pages to avoid errors.")
parser.add_argument("--nocover",  action='store_true', help="Default behavior is to treat the second page as the back cover. Speficy to treat the last page as the back cover.")
args = parser.parse_args()

if args.verbose == True:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
else:
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

force = False
if args.force == True:
    force = True

nocover = False
if args.nocover == True:
    nocover = True
    
def gen_blanks(num=1):
    for i in range(num):
        #os.system(f'cp ./blank [logic that finds and adds the next page in sequence]
        logging.warning(f'genorate blank page placeholder function; no functionality!')
        exit()

def clear_cache():
    cache_files = glob.glob("../cache/*")
    logging.info(f'clearing cach')
    for file in cache_files:
        os.remove(file)

current_pair_of_pages = 0
def move_two_pages():
    global current_pair_of_pages
    file = jpg_files[current_pair_of_pages]
    os.system(f"cp {file} ../cache/img01.jpg")
    os.system(f"cp {file} ../cache/img03.jpg")
    os.system(f"cp {file} ../cache/img05.jpg")
    os.system(f"cp {file} ../cache/img07.jpg")

    file = jpg_files[len(jpg_files)-1-current_pair_of_pages]
    os.system(f"cp {file} ../cache/img02.jpg")
    os.system(f"cp {file} ../cache/img04.jpg")
    os.system(f"cp {file} ../cache/img06.jpg")
    os.system(f"cp {file} ../cache/img08.jpg")

    current_pair_of_pages += 1

        
#2 clear cache;
clear_cache()

#3 identify if there are the number of jpgs is a multipule of four. if there is less than four, abort. If there is a multipule of four, continue. If -f is specified, add blanks. otherwise abort;

jpg_files = glob.glob("img*.jpg")
num_jpgs = len(jpg_files)

if num_jpgs < 4:
    logging.warning(f'Less than four imgs detected. Aborting')
    exit()

if not num_jpgs % 4:
    pass

if num_jpgs % 4:
    if force:
        gen_blanks(4 - (num_jpgs % 4))
        jpg_files = glob.glob("img*.jpg")
    else:
        logging.warning(f'number of imgs is not a multipul of four. Aborting. Try -force')
        
#4 unless --nocover is specified, modify the jpg_files list: move 1st image to the end;

if not nocover:
    jpg_files.insert(len(jpg_files), jpg_files.pop(0))

#7 repeat 5 & 6 until all pages have been processed.

for i in range(int(len(jpg_files)/2)):

    #5 copy 2 jpgs to cache: the first and last, then second and second to last...;    
    logging.info(f'moving pages to cache')
    move_two_pages()
    
    #6 render pdf to cache;
    
    html_path = os.path.abspath('../html/generic.html')
    logging.info(f'begining render {current_pair_of_pages}')
    converter.convert(f'file:///{html_path}', f'../cache/render{current_pair_of_pages:0=2d}.pdf')    

#8 combine the cached pdfs to PRINT.pdf.
os.system(f'pdfunite ../cache/*.pdf PRINT.pdf')

#9 clear cache
clear_cache()

#10 exit
exit()
