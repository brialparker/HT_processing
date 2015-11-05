for dir in $(find . -type d); do
    zip -r -X  "$dir".zip "$dir"
done