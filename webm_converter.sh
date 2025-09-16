#!/bin/bash

# Converts all .webp photos in ~/Pictures and /Pcitures/wp to a png :)
photo_dir="$HOME/Pictures/"
wp_dir="$HOME/Pictures/wp"

conv (){
    for file in "$1"/*; do
        ext="${file##*.}"
        if [ "$ext" == "webp" ]; then
            fileName="${file##*/}"
            targetFile="${fileName%%.*}.png"
            echo "Converting $fileName to $targetFile"
            convert "$file" "$photo_dir/$targetFile"
            rm "$file"
        fi
    done
}

conv "$photo_dir"
conv "$wp_dir"
