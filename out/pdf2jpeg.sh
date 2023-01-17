echo "Working...";
rm img*;
pdfseparate source.pdf img%d.pdf;
for i in img*; do convert -density 300 -background white -alpha remove $i $(perl -e 'print $ARGV[0] =~ s/\.[^.]+$//r' $i).jpg; rm $i; done;
echo "Done!";
