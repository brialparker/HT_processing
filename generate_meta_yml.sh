#!/bin/bash

for file in $(find . -name '00000001.tif');
do
        parentdir=$(dirname "$file")
        exiftool -j -FileModifyDate -XResolution  "$file" | python json2yaml.py > $parentdir/meta.yml
done