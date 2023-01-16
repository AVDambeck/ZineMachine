#This is really bad but my lazy file names are comeing to bite me. hacky fix for now.
for i in img*; do mv $i $(perl -e 'print $ARGV[0] =~ s/\.[^.]+$//r' $i).pdf.jpg; done;
