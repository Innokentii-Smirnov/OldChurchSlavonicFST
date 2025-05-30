filepath="Segmentation/Segmentation.foma"
directory=$(dirname $filepath)
name=$(basename $filepath .foma)
binary=$name.bin
cd $directory
foma -e "source $name.foma" -e "push $name" -e "save stack $binary" -e "sigma" -e "exit"
echo "Created Foma binary $binary."
cd ..
flookup -s " ← " -b "$directory/$binary" < input.txt > output.txt
python evaluate.py
