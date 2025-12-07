# Install dependencies
```bash
apt install foma
```
Please use your system's packet manager (e. g. brew) in place of apt if necessary.
You can also download a binary from https://fomafst.github.io/

# Test
The following script will compile the finite-state transducer,
apply it to the data in input.txt,
compare the output to corr.txt and print the precision.
```bash
./test.sh
```

For recall and accuracy, run
```bash
./extended_evaluation.sh
```
