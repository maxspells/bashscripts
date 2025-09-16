#!/bin/bash

WPDIR="$HOME/Pictures/wp"

FILE=$(find "$WPDIR" -type f \( -iname '*.jpg' -o -iname '*.png' \) | shuf -n 1)

feh --bg-scale "$FILE"
