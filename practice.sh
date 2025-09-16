#!/bin/bash

# this is a comment, bash ignores it



# echo prints shit
echo "This is how you print to a terminal"

#this is how you set variables
nameStr="Max"
#no spaces between var=setting

#call vars with $varname
echo "Heyyyy $nameStr!"


# use read to get user input
echo "Who is your favorite pokemon?"
read favorite_pokemon
echo "Wow $favorite_pokemon is a good choice"


#Conditionals (if statements)

echo "Pick any number"
read num

# NEED SPACES [ "$num" -gt 10 ] not ["$num" -gt 10]
if [ "$num" -gt 10 ]; then # -gt greater than, -lt lesser than, -eq equals
    echo "That's bigger than 10 wow!"
else
    echo "That's small or equal to 10"
fi

# Loopin

count=1
while [ $count -le 5 ]; do
    echo "Count is at $count"
    count=$((count+1)) #why two parentheses? #why the $ sign before this?
    #Double ((...)) → is arithmetic expansion (Bash’s math mode).
done

#for loop
for file in *sh; do
    echo "Script: $file"
done

#function
say_hello(){
    echo "Hello, $1!"
}
# $1 is the first arg passed in, $2 for second etc
say_hello "Max"
say_hello "Cory"

# ASK about why var in quotes
# ASK what fi does



