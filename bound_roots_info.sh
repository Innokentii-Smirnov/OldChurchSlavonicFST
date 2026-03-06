grep 'r;$' src/Morphotactics/Morphotactics.lexc | cut -d ' ' -f 1 | while read -r root; do
  grep -F "$root" corr.txt
done | sed '='
