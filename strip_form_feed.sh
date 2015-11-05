#!/bin/bash

for file in $(find . -name '*.txt')
do
        sed -i "" 's/\^L//' "$file"
done