# Make 8 Fold Zines Easy!
This is an HTML tool to page set small format zines, specifically 8fold and 4panel. Forked from [@rowan_m](https://twitter.com/rowan_m)'s site [/zine-machine.glitch.me](https://zine-machine.glitch.me/). There they go over the method of folding the zine, and how the css would work, but their actual code isn't exactly what I wanted: Tool that page sets a document made with another program.

There are also some tools to help with processing into a print ready document. Although this does use html as a markup language, it's indented use-case is as a local file on a Linux system.

# Usage
First format you zine in the document editor of your choice, and export as either a PDF or JPG sequence. For octiletter, it must be 8 pages, 2.75x4.25 inches. For demiletter, 2 pages, 4.5x11.  Remember to take into account the print margins when making the zine, zine machine does not.

Go to the demiletter/pages or octiletter/pages directory. Put your PDF there and rename it "source.pdf". Run the bash script provided. You'll need imagemagick and pdfseperate. Alternatively export your pages to those image locations (img1.pdf.jpg, etc) manually.

Open the HTML (linked below) for your desired print format with your browser. Ctl+P to Print with no margins. For 4panel, you'll then need to merge the front and back pages using pdfunite or equivalent.

# Support
This is a rather hacky tool. Feel free to reach out if you are having trouble, no promises if I can actually help tho.
