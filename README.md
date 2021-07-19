# Make 8 Fold Zines Easy!
You can learn how to make 8 page [zines](https://en.wikibooks.org/wiki/Zine_Making/Putting_pages_together) here. This is a tool to convert an 8 page document into an 8 page zine. Most of this was borrowed from [@rowan_m](https://twitter.com/rowan_m)'s site [/zine-machine.glitch.me](https://zine-machine.glitch.me/). There they go over the method of folding the zine, and how the css would work, but don't give the actual code to do it from your own images. I spent an hour coping that and tweaking the numbers to fit right, and figured I'd share. 

# Usage
The img directory contains img-0.png through img-8.png. These are your eight pages. Included as an example is my game [Robots](https://github.com/AVDambeck/Robots). Any images should work, but included is an [ImageMagick](https://imagemagick.org) command to split pdfs into a png for each page. 

Simply download the repository and put it somewhere connivent. Put your pages in img, and then open index.html in your browser. Press print and there you go. You can print it to a pdf if you want to send copies that way, or send it straight to your printer.

If you want to remove the borders, simply comment or delete lines 15 and 16 in master.css. 

I'm printing on letter paper. I suspect that if you had your zine pages proportioned to ISO standards, that it would just work with A4. If not you can tweak the css for it.
