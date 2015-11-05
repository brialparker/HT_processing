for dir in $(find . -type d); do
    md5 -r "$dir"/* | sed "s:$dir/::" > "$dir/checksum.md5"
done