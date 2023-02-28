#!python
"""
Abstract:
00. This is a program which will take each jpg in a directory, crop it, and replace the orignal. Intended for scans of physical art. Specify the dimenstions to be cropped with with x/ylen/off. Unit is inches.
1. Define and import.
2. Catch dimenstional info from flags.
    2.1 Catch var.
    2.2 Save to var or keep default.
    2.3 Compute px mesurment.
3. for each jpg, convert. 
5. Exit.
"""

# Step 1.
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

# Step 2.
# Catch user input from flags.
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose",  action='store_true', help="Increase verbosity.")
parser.add_argument("-x", "--xlen", type=float, help="Horizontal width of the image.")
parser.add_argument("-X", "--xoff", type=float, help="Horizontal width of croparea to the left of the image.")
parser.add_argument("-y", "--ylen", type=float, help="Vertical hieght of the image.")
parser.add_argument("-Y", "--yoff", type=float, help="Vertical hieght of croparea to the top of the image.")
args = parser.parse_args()

if args.verbose == True:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
else:
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Store input to var.
if args.xlen != xlen:
    xlen = args.xlen
    logging.info(f'xlen set from flag, = {args.xlen}.')
else:
    logging.info(f'xlen set from default, = {xlen}.')

if args.xoff != xoff:
    xoff = args.xoff
    logging.info(f'xoff set from flag, = {args.xoff}.')
else:
    logging.info(f'xoff set from default, = {xoff}.')

if args.ylen != ylen:
    ylen = args.ylen
    logging.info(f'ylen set from flag, = {args.ylen}.')
else:
    logging.info(f'ylen set from default, = {ylen}')

if args.yoff != yoff:
    yoff = args.yoff
    logging.info(f'yoff set from flag, = {args.yoff}.')
else:
    logging.info(f'yoff set from default, = {yoff}.')

# Compute px mesurment.
xlen_px = inch_to_px(xlen)
xoff_px = inch_to_px(xoff)
ylen_px = inch_to_px(ylen)
yoff_px = inch_to_px(yoff)
print(xlen_px)
logging.info(f'calculated px mesurments to xlen={xlen_px}, xoff={xoff_px}, ylen={ylen_px}, yoff={yoff_px}.')

# Step 3.
# This part could also be optimized with paralel processing. Not needed at current scale.
logging.info('Begin cropping.')
subprocess.run(f"for i in *.jpg; do magick $i -crop {xlen_px}x{ylen_px}+{xoff_px}+{yoff_px} $i; done;", shell=True)

# Step 4
logging.info('end of program.')
exit()
