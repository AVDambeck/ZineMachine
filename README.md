# Make 8 Fold Zines Easy!
This is an HTML tool to page set small format zines, specifically 8fold and accordian. 

Using html ~~stolen~~ borrowed from [@rowan_m](https://twitter.com/rowan_m)'s site [/zine-machine.glitch.me](https://zine-machine.glitch.me/). There they go over the method of folding the zine, and how the css would work, but their actual code isn't exactly what I wanted: Tool that page sets a document made with another program. Now the project also has numerous other tools for automatically croping, deviding, and rendering print files. 

# Installation
This is for linux :)

First install python, pypdf, and pyhtml2pdf.

Dowload and unzip Zine Machine into a convinent location.

Navigate to /ZineMachine/files. This is where you operate ZineMachine from.

# Usage
First format you zine in the editor of your choice, and export it to SOURCE.pdf. For accordian, it must be 8 pages, 2.75x4.25 inches. Rememer to take into account the print margins when making the zine, zine machine does not. 

Run pdf2jpg.sh.

Run render-accordian.py

Print and enjoy!

## Varations

Use render-8fold to have be 8fold instead of accordian. This is less paper efficiant but doesnt require a duplex printing. 

Scan physical media, then use crop.py to crop it. Hand illustration and collage are pretty.

Make two 11x4.25 pages with four columns, then use the devider.py with octi_on_demi.json to make it into 8 2.75x4.25 pages. This is a smoother workflow when using an office program. 

# Functions

clear.sh
	Removes all imgs.
crop.py
	Crops each of the imgs.
	crop.py [-h] [-v] [-x XLEN] [-X XOFF] [-y YLEN] [-Y YOFF].
	X and Y off specify the top left corner of the print area. x and y specify the dimensions of the crop area. Units in inches.
divide.py
	Crops document pages out of a SOURCE.pdf with multiple document pages per pdf page. Think a book scan with two book pages in each scan. Be sure to specify a template from divider_templates/
	divide.py [-h] [-v] [-t TEMPLATE]
join-front-back.sh
	joins FRONT.pdf and BACK.pdf to UNITE.pdf
jpg2pdf.sh
	Reverts the img sequence to UNITE.pdf.
pdf2jpg
	Seperates SOURCE.pdf into imgs.
render*.py
	Makes the imgs into a print ready zine of the specified format. Exports to PRINT.pdf

# Support
This is a rather hacky tool. Feel free to reach out if you are having trouble, no promises if I can actually help tho.
