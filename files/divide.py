"""
pdf page will be called page, document page will be called leaf.

Abstract:
00. Often in scanning documents, the result will have more than one leaf per pdf page. This is a program which inputs such a result, and outputs the isolated leaf;
0. This is a program which takes an input SOURCE.pdf and a crop_template.json. Outputs a jpg sequence of leaf cropped out of the SOURCE.pdf pages, according to the specifications in crop_template.json;
1. import and define;
2. import crop_template.json specified with cli flag;
3. clear any images in files/ && clear cache;
4. extract hte first of the pdf as a png to cache;
5. for each leaf specified in crop_template.json,  crop and export jpg;
6. remove first page from cache;
7. repeat 4-6 with rest of the pages;
8. exit;
"""

#1 import and define.
import json
import argparse
import logging
import os
import glob
from pypdf import PdfReader, PdfWriter
import subprocess

reader = PdfReader("SOURCE.pdf")
number_of_pages = len(reader.pages)
leaf_count = 1
output_dpi = 300

# Define inch_to_px function.
def inch_to_px(inch, dpi=output_dpi):
    return(inch*dpi)

#2 catch json from flag
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action='store_true', help="Increase verbosity.")
parser.add_argument("-t", "--template", help="location of crop template.")
args = parser.parse_args()

if args.verbose == True:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
else:
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if args.template == None:
    logging.warning(f'No template specified. Did you forget --template?')
    exit()
else:
    f = open(args.template)
    template = json.load(f)
    if template["message"] != "":
        logging.warning(f'template message: {template["message"]}')
#3 clear imgs and cache
jpg_files = glob.glob("*.jpg")
for file in jpg_files:
    os.remove(file)
cache_files = glob.glob("../cache/*")
for file in cache_files:
    os.remove(file)

for page_num in range(0,number_of_pages):
    #4 extract first page of page of pdf to cache
    writer = PdfWriter()
    writer.add_page(reader.pages[page_num])
    with open("../cache/page.pdf", "wb") as f:
        writer.write(f)

    #5 for each document page specified in crop tempalte, crop and export .jpg
    # This part is particularly slow for longer files. I don't think its a big enough issue to address, but this would be fairly easy to parrelelize with asyncio. Something like extreact all the pages at once, and then have a sepreate process for each page. If your really nuts you could try do a seperate process for each leaf.
    logging.info(f'page {page_num}')
    for leaf in template["pages"]:
        xlen_px = inch_to_px(leaf[0])
        ylen_px = inch_to_px(leaf[1])
        xoff_px = inch_to_px(leaf[2])
        yoff_px = inch_to_px(leaf[3])
        try:
            rotate = leaf[4]
        except:
            pass
        leaf_name = f"img{leaf_count:02}.jpg"
        logging.info(leaf_name)
        try:
            subprocess.run(f"magick -density {output_dpi} ../cache/page.pdf -crop {xlen_px}x{ylen_px}+{xoff_px}+{yoff_px} -rotate {rotate} {leaf_name};", shell=True)
        except:
            subprocess.run(f"magick -density {output_dpi} ../cache/page.pdf -crop {xlen_px}x{ylen_px}+{xoff_px}+{yoff_px} {leaf_name};", shell=True)
        leaf_count += 1

    #6
    os.remove("../cache/page.pdf")

exit()
