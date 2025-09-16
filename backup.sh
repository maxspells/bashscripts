#!/bin/bash

# _Paths_
# Target drive
MEDIA="/mnt/media"

# Core directories
PHOTO_SRC="$HOME/Pictures"
VIDEO_SRC="$HOME/Videos"
APPS_SRC="$HOME/Applications"
ARCHIVES_SRC="$HOME/Archives"

# Destination directories
PHOTO_DST="$MEDIA/photos"
VIDEO_DST="$MEDIA/videos/videos"
FILES_DST="$MEDIA/files"


clear
query_directory (){ # ARG1 should be source directory
    local dir="$1"
    while true; do
        echo
        local size
        size=$(du -sh "$dir")
        echo "Total size of files: $size"
        echo "Do you want to backup $dir? yes/no:"
        read -r choice
        case "$choice" in
            y|yes|YES|Yes|Y)
                echo "Backing up $dir..."
                backup_directory "$dir"
                break
                ;;
            n|no|N|NO|No)
                echo "Skipping $dir..."
                break
                ;;
            *)
                echo "Invalid input"

        esac
    done
}

backup_directory (){ # ARG1 should be source directory
    local src="$1"
    local type="${src##*/}"
    case $type in
        Pictures)
            local dest="$PHOTO_DST"
            ;;
        Videos)
            local dest="$VIDEO_DST"
            ;;
        Applications)
            local dest="$FILES_DST"
            ;;
        Archives)
            local dest="$FILES_DST"
            ;;
        *)
            echo "Something went wrong here in backup_directory()"
            echo "type = $type"
            ;;
    esac
    echo "$dest" # Testing to see if code works before I move files
    move_all_files "$src" "$dest"
}

move_all_files(){ # ARG1 should be the source directory, ARG2 should be the destination directory
    local src="$1"
    local dst="$2"
    for file in "$src"/*; do
        if [ -f "$file" ]; then
            echo "Backing up $file..."
            mv "$file" "$dst"
        fi
    done
}

query_directory "$PHOTO_SRC"
query_directory "$VIDEO_SRC"
query_directory "$APPS_SRC"
query_directory "$ARCHIVES_SRC"
