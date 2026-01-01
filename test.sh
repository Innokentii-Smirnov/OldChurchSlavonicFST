filepath="src/Segmentation/Segmentation.foma"
directory=$(dirname "$filepath")
name=$(basename "$filepath" .foma)
binary="$name.bin"
CompileFST/CompileFST.sh "$filepath"
flookup -s " ← " -b "$directory/$binary" < input.txt > output.txt
python evaluate.py
