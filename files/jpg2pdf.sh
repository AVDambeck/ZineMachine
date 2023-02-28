for i in img*; do convert $i ../cache/$i.pdf; done;
pdfunite ../cache/* UNITE.pdf;
rm ../cache/*;
