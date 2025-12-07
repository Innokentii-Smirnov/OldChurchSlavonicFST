filepath="Segmentation/Segmentation.foma"
directory=$(dirname $filepath)
name=$(basename $filepath .foma)
binary=$name.bin
cd $directory
foma -e "source $name.foma" -e "push $name" -e "save stack $binary" -e "sigma" -e "exit"
echo "Created Foma binary $binary."
cd ..
tr -d '12/ *' < input.txt | flookup -s " ← " -b "$directory/$binary" > output.txt
python evaluate.py
