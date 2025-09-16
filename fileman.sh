#!/bin/bash

echo "File Organizer v2: Now with more bash!"
echo "Organizing files..."

# Core downloads directory defined here
downloads_dir="$HOME/Downloads"

# Other directories for sorting files into
photo_dir="$HOME/Pictures"
app_dir="$HOME/Applications"
archives_dir="$HOME/Archives"
docs_dir="$HOME/Documents"
music_dir="$HOME/Music"
video_dir="$HOME/Videos"

mkdir -p "$photo_dir" "$music_dir" "$docs_dir" "$app_dir" "$archives_dir" # Makes target directories if they don't already exist

get_filetype(){
    local ext="${1##*.}" # Get the file extension
    ext="${ext,,}" # Converts to lowercase
    case $ext in
        jpg|jpeg|png|gif|bmp|webp)
            echo "photo"
            ;;
        mp3|wav|flac|mid)
            echo "music"
            ;;
        pdf|doc|docx|txt)
            echo "document"
            ;;
        exe|appimage)
            echo "executable"
            ;;
        zip|7z|rar)
            echo "archive"
            ;;
        mp4|mkv|avi|mov|wmv|flv|webm|mpeg|mpg|m4v|ogv)
            echo "video"
            ;;
        *)
            echo "other"
            ;;
    esac
}

# Arg 1 should be file, Arg 2 should be filetype
move_file(){
    local file="$1"
    local type="$2"
    echo "Moving $file to $type folder"
    case "$type" in
        photo)
            mv "$file" "$photo_dir"
            ;;
        music)
            mv "$file" "$music_dir"
            ;;
        document)
            mv "$file" "$docs_dir"
            ;;
        executable)
            mv "$file" "$app_dir"
            ;;
        archive)
            mv "$file" "$archives_dir"
            ;;
        video)
            mv "$file" "$video_dir"
    esac
}


count=0
otherCount=0
for file in "$downloads_dir"/*; do
    if [ -f "$file" ]; then
        filename="${file##*/}"
        type=$(get_filetype "$filename")
        if [ "$type" != "other" ]; then
            move_file "$file" "$type"
            count=$((count+1))
        else
            otherCount=$((otherCount+1))
        fi
    fi
done
echo "$count files successfully sorted"
echo "$otherCount unsorted files left in $downloads_dir"
echo "Done!"
