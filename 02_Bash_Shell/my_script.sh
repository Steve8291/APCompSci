#!/bin/bash

echo "Hello World!"
echo -e "\nMy name is Steve\n"

# Take user input
read -p "Enter a number between 1 and 10: " user_num
echo "Your number was $user_num"

read -p "Enter a second number between 1 and 10: " user_num2
echo "Your number was $user_num2"

## Integer Comparison Operators:
# -eq 	Integer equality
# -ne 	Integer inequality
# -lt 	Integer less than
# -le 	Integer less than or equal to
# -gt 	Integer greater than
# -ge 	Integer greater than or equal to

## Arithmetic Expansion Operators:
# (( a > b ))
# (( a >= b ))
# (( a == b ))
# (( a != b ))
# && 	Logical AND
# || 	Logical OR

if [[ "$user_num" -gt 10 ]]; then
    echo "You entered a number that was too big!"
elif [ "$user_num" -lt 0 ]; then
    echo "You entered a number that was too small"
else
    # Addition
    sum=$((5 + user_num))
    echo "$user_num + 5 = $sum"
fi

# Using a regular expression
if [[ "$user_num" =~ ^([0-9]|10)$ ]]; then
    echo "You are awesome and entered: $user_num"
else
    echo "You can't follow directions"
fi

add_nums=$((user_num + user_num2))
echo "The sum of your numbers is $add_nums"

echo ""
echo "####### Now let's validate your input to be between 1 and 10 #######"

user_num=0
while [[ "$user_num" -le 0 || "$user_num" -gt 10 ]]; do
    read -p "Enter a number between 1 and 10: " user_num
    echo "You entered: $user_num"
done

echo "Thank you! You entered $user_num"

while true; do
    echo "Oh no I'm an infinite loop! Press [CTRL+C] to stop me!"
    # sleep 2
done

# Colored output in a here doc:
# Define some tput commands for colors
RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
RESET=$(tput sgr0) # Reset attributes

cat <<- EOF
        ${RED}This text is red.${RESET}
        ${GREEN}This text is green.${RESET}
        This text is normal.
EOF