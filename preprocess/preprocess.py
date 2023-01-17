#!python
"""
This is a program which will take each page of a pdf, crop it, and output as a jpg. Intended for scans of physical art. Specify the dimenstions to be cropped with with x/ylen/off. Unit is inches.

Abstract:
00. Define and import.
0. Catch dimenstional info from flags.
    0.1 Catch var.
    0.2 Save to var or keep default.
    0.3 Compute px mesurment.
1. Remove old imgs.
2. Split the pdf into jpgs.
        2.1 Split the pdf.
        2.2 For each file convert.
3. Crop each of the jpgs.
4. Remove intermedate images.
5. Exit.

Notes:
In step 1, if there are no imgs, it prints an error. doesnt inhibit function; not going to patch.
Between step 2.2 and 3 theres a hacky thing where I convert to pdf>png>jpg instead of clerverer filename handling, or just doing it in one step.
"""

# Step 00.
import argparse
import subprocess
import logging


# Define default values.
xlen = 5.5
xoff = 2.375
ylen = 8.5
yoff = 0.5
output_dpi = 300

# Define inch_to_px function.
def inch_to_px(inch, dpi=output_dpi):
    return(inch*dpi)

# Step 0.
# Catch user input from flags.
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",  action='store_true', help="Increase verbosity.")
parser.add_argument("-x", "--xlen", help="Horizontal width of the image.")
parser.add_argument("-X", "--xoff", help="Horizontal width of croparea to the left of the image.")
parser.add_argument("-y", "--ylen", help="Vertical hieght of the image.")
parser.add_argument("-Y", "--yoff", help="Vertical hieght of croparea to the top of the image.")
args = parser.parse_args()

if args.verbose == True:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
else:
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Store input to var.
if args.xlen:
    xlen = args.xlen
    logging.info(f'xlen set from flag, = {args.xlen}.')
else:
    logging.info(f'xlen set from default, = {xlen}.')

if args.xoff:
    xoff = args.xoff
    logging.info(f'xoff set from flag, = {args.xoff}.')
else:
    logging.info(f'xoff set from default, = {xoff}.')

if args.ylen:
    ylen = args.ylen
    logging.info(f'ylen set from flag, = {args.ylen}.')
else:
    logging.info(f'ylen set from default, = {ylen}')

if args.yoff:
    yoff = args.yoff
    logging.info(f'yoff set from flag, = {args.yoff}.')
else:
    logging.info(f'yoff set from default, = {yoff}.')

# Compute px mesurment.
xlen_px = inch_to_px(xlen)
xoff_px = inch_to_px(xoff)
ylen_px = inch_to_px(ylen)
yoff_px = inch_to_px(yoff)
logging.info(f'calculated px mesurments to xlen={xlen_px}, xoff={xoff_px}, ylen={ylen_px}, yoff={yoff_px}.')

# Step 1.
logging.info('removing old imgs. prints error to consol if no imgs.')
subprocess.run("rm img*", shell=True)

# Step 2.
# Split pdf.
logging.info('seperating pdf, this may take a moment.')
subprocess.run(["pdfseparate", "source.pdf", "img%d.pdf"])

# Converting to jpg.
# This part could be optimized with paralel processing. Puyt the loop in python and use asyncio or something. Its not so long that I actually bother (about 2 minutes on my i7). If you wanted to process at 600 dpi, or a longer document, it could be worth while.
logging.info('converting from pdf, this may take a moment.')
subprocess.run(f"for i in img*; do convert -density {output_dpi} -background white -alpha remove $i $(perl -e 'print $ARGV[0] =~ s/\.[^.]+$//r' $i).png; done;", shell=True)

# Step 3.
# This part could also be optimized with paralel processing, as above.
logging.info('Begin cropping.')
subprocess.run(f"for i in *.png; do magick $i -crop {xlen_px}x{ylen_px}+{xoff_px}+{yoff_px} $(perl -e 'print $ARGV[0] =~ s/\.[^.]+$//r' $i).jpg; done;", shell=True)

# Step 4
logging.info('removing uncrops and pdf')
subprocess.run('find . -type f -name "*.pdf" ! -name "source.pdf" -delete', shell=True)
subprocess.run('rm *png', shell=True)

# Step 5
logging.info('end of program.')
exit()
