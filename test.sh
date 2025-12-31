filepath="Segmentation/Segmentation.foma"
directory=$(dirname "$filepath")
name=$(basename "$filepath" .foma)
binary="$name.bin"
CompileFST/CompileFST.sh "$filepath"
tr -d '12/ *' < input.txt | flookup -s " ← " -b "$directory/$binary" > output.txt
python evaluate.py
